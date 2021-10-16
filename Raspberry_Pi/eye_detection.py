


import cv2

def get_cascades():
    # Initializing the face and eye cascade classifiers from xml files
    filename1 = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(filename1)

    filename2 = cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
    eye_cascade = cv2.CascadeClassifier(filename2)

    return face_cascade, eye_cascade


face_cascade, eye_cascade = get_cascades()


# Starting the video capture
cap = cv2.VideoCapture(0)
ret, img = cap.read()

# we have to pre-define message and color so that my IDE will SHUT UP ABOUT IT. It's fine if you delete the next 2 lines of code, but my IDE loves to bug me about it so here we are
message = ""
color = (0, 0, 0) # color is BGR instead of RGB for some reason. Why? bc opencv sucks

while (ret):
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

        #classifying eyes and storing all eyes found in an array:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face_roi = gray[y:y + h, x:x + w]
        roi_face_clr = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_roi, 1.3, 5, minSize=(50, 50))

        if (len(eyes) >= 2):
            message = "eye detected"
            color = (0, 255, 0) # green

        else:
            message = "No eyes detected"
            color = (255, 0, 0) #blue

    cv2.putText(img, message, (70, 70), cv2.QT_FONT_BLACK, 3, color, 2)

    cv2.imshow('img', img)
    a = cv2.waitKey(1)
    if (a == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()
