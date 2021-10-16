import cv2
from time import perf_counter
from typing import Dict, Callable, Tuple, Any
import os


def get_cascades() -> Tuple[Any, Any]:
    """
    Dynamically finds the cascades, and returns 2 cascade objects (face, eye)
    :return: face_cascade, eye_cascade
    """
    # Initializing the face and eye cascade classifiers from xml files

    try:
        file_path = os.path.dirname(os.path.realpath(__file__))
        filename1 = f"{file_path}/media/haarcascade_frontalface_default.xml"
        filename2 = f"{file_path}/media/haarcascade_eye_tree_eyeglasses.xml"
        face_cascade = cv2.CascadeClassifier(filename1)
        eye_cascade = cv2.CascadeClassifier(filename2)
        # print(filename1, filename2)

    except:
        filename1 = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(filename1)

        filename2 = cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
        eye_cascade = cv2.CascadeClassifier(filename2)
    return face_cascade, eye_cascade


def start_detection(
    threshold_to_function: Dict[
        float, Tuple[Callable, bool]
    ],  # Callable just means function
    print_logs: bool = True,
    show_window_video: bool = True,
) -> None:
    """
    Look at some examples to better understand how this works
    :param threshold_to_function: A dictionary that maps float values to functions. For example, if you want the program to execute
    the print function when the eyes are closed for more than two seconds, and you want this to be repeatable,
     then the threshold_to_function argument would be {2: (print, True)}
    :param print_logs: the function outputs for debugging
    :param show_window_video: shows you what the ai is seeing in real time (again, mostly for debugging)
    :return: None
    """
    face_cascade, eye_cascade = get_cascades()

    # Starting the video capture
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()

    eyes_last_seen_open_timestamp = perf_counter()

    while ret:
        ret, img = cap.read()
        # Converting the recorded image to grayscale bc it doesn't work if it's not grayscale.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Applying filter to remove impurities
        gray = cv2.bilateralFilter(gray, 5, 1, 1)

        # Detecting the face for region of image to be fed to eye classifier
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(200, 200))

        message = "No face detected"
        color = (0, 0, 255)  # red

        for (x, y, w, h) in faces:

            # classifying eyes and storing all eyes found in an array:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_roi = gray[y : y + h, x : x + w]
            eyes = eye_cascade.detectMultiScale(face_roi, 1.3, 5, minSize=(50, 50))

            if len(eyes) >= 2:
                message = "eye detected"
                color = (0, 255, 0)  # green
                eyes_last_seen_open_timestamp = perf_counter()  # updating timestamp

            else:
                message = f"closed for {round(perf_counter() - eyes_last_seen_open_timestamp, 2)}"
                color = (255, 0, 0)  # blue
        if len(faces) == 0:
            eyes_last_seen_open_timestamp = (
                perf_counter()
            )  # updating timestamp bc there's no face

        how_long_eyes_have_been_closed = perf_counter() - eyes_last_seen_open_timestamp

        to_pop = []  # list of entries to pop
        for t in threshold_to_function:
            if how_long_eyes_have_been_closed > t:
                # the eyes have been closed for more than t seconds, let's execute the neccesary function:
                if print_logs:
                    print(
                        "eyes have been closed for",
                        how_long_eyes_have_been_closed,
                        "executing",
                        threshold_to_function[t][0],
                    )
                threshold_to_function[t][0]()

                if not threshold_to_function[t][1]:
                    to_pop.append(t)

        for t in to_pop:
            del threshold_to_function[
                t
            ]  # deleting this entry from the dictionary so it's not repeated

        if print_logs:
            print(message)

        if show_window_video:
            cv2.putText(img, message, (70, 70), cv2.QT_FONT_BLACK, 3, color, 2)
            cv2.imshow("img", img)

        a = cv2.waitKey(1)
        if a == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    import events

    def person_is_sleeping():
        events.on_sleep(wait_time_between_sounds=0.5, decibel_increase=10, repetition=1)

    def oh_no_youre_dying():
        events.on_crash()

    # if person sleeps for more than 2 seconds, the alarm will go off. The process is repeatable (as long as the eyes are
    # closed for more than 2 seconds, this function keeps executing repeatedly)

    # if the person closes their eyes for more than 5 seconds, "911" will be contacted. This is done only once, it does not repeat.
    # so even if you close your eyes for 1000 seconds, "911" will be contacted only once
    function_maps = {1: (person_is_sleeping, True), 10: (oh_no_youre_dying, False)}

    start_detection(function_maps, False, True)
