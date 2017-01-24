import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

vc = cv2.VideoCapture(0)

while -1: 
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,171),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,188,255),2)

        smiling = smile_cascade.detectMultiScale(roi_gray, 1.7, 5)
        for (sx,sy,sw,sh) in smiling:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(240,19,93),2)

    cv2.imshow('WebDetect',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        vc.release()
        cv2.destroyAllWindows()

