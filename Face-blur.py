import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
side_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')


while True:
    ret, frame = cap.read()

    bigger_frame = cv2.resize(frame, (0,0), fx=2, fy=2)
    frame = bigger_frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flipped_gray = cv2.flip(gray, 1)

    faces = face_cascade.detectMultiScale(gray, 1.05, 5)

    left_side_faces = side_face_cascade.detectMultiScale(gray, 1.1, 5)
    right_side_faces = side_face_cascade.detectMultiScale(flipped_gray, 1.1, 5)
    

    for(x, y, w, h) in faces:
        faceROI = frame[y:y+h,x:x+w]
        blurred = cv2.blur(faceROI, (45, 45))
        frame[y:y+h, x:x+w] = blurred

    for(x, y, w, h) in left_side_faces:
        faceROI = frame[y:y+h,x:x+w]
        blurred = cv2.blur(faceROI, (45, 45))
        frame[y:y+h, x:x+w] = blurred

    for(x, y, w, h) in right_side_faces:
        faceROI = frame[y:y+h,x:x+w]
        blurred = cv2.blur(faceROI, (45, 45))
        frame[y:y+h, x:x+w] = blurred

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()