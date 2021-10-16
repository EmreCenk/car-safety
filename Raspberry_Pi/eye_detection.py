import cv2
from time import perf_counter


def get_cascades():
    """
    Dynamically finds the cascades, and returns 2 cascade objects (face, eye)
    :return: face_cascade, eye_cascade
    """
    # Initializing the face and eye cascade classifiers from xml files
    filename1 = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(filename1)

    filename2 = cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
    eye_cascade = cv2.CascadeClassifier(filename2)

    return face_cascade, eye_cascade


def start_detection(print_logs: bool = True, show_window_video: bool = True):
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
                message = "No eyes detected"
                color = (255, 0, 0)  # blue

        how_long_eyes_have_been_closed = perf_counter() - eyes_last_seen_open_timestamp
        if how_long_eyes_have_been_closed > 2 and print_logs:
            # the eyes have been closed for more than two seconds
            print("eyes have been closed for", how_long_eyes_have_been_closed)

        if show_window_video:
            cv2.putText(img, message, (70, 70), cv2.QT_FONT_BLACK, 3, color, 2)
            cv2.imshow("img", img)

        a = cv2.waitKey(1)
        if a == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_detection(True, False)
