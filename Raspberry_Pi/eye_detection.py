


import cv2

def get_cascades():
    # Initializing the face and eye cascade classifiers from xml files
    filename1 = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(filename1)

    filename2 = cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
    eye_cascade = cv2.CascadeClassifier(filename2)

    return face_cascade, eye_cascade


face_cascade, eye_cascade = get_cascades()
