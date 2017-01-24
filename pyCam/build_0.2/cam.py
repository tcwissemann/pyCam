import cv2
import numpy as np
from twilio.rest import TwilioRestClient 
import time

#importing modules ^^

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
glasses_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

vc = cv2.VideoCapture(0)

#finding default camera ^^

while -1: 
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 2)
    
#converting img frame by frame to suitable type ^^

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,171),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") #account_sid, auth_token for twilio accaount.

        client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx", #user number, twilio number 
                       body="Alert: person(s) on property.") #messege
        
        time.sleep(300)
        
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,188,255),2)
        client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") #account_sid, auth_token for twilio accaount.

        client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx", #user number, twilio number 
                       body="Alert: person(s) on property.") #messege
        
        time.sleep(300)
        
    smiling = smile_cascade.detectMultiScale(roi_gray, 1.7, 5)
    for (sx,sy,sw,sh) in smiling:
        cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(240,19,93),2)
        client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") #account_sid, auth_token for twilio accaount.

        client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx", #user number, twilio number 
                       body="Alert: person(s) on property.") #messege
        
        time.sleep(300)
        
    glasses = glasses_cascade.detectMultiScale(roi_gray, 1.7, 5)
    for (gx,gy,gw,gh) in glasses:
        cv2.rectangle(roi_color,(gx,gy),(gx+gw,gy+gh),(241,18,92),2)
        client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") #account_sid, auth_token for twilio accaount.

        client.messages.create(to="+1xxxxxxxxxx", from_="+1xxxxxxxxxx", #user number, twilio number 
                       body="Alert: person(s) on property.") #messege
    
        time.sleep(300)
        
#look for features, draw box on features, sends sms upon sight of features ^^

    cv2.imshow('WebDetect',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        vc.release()
        cv2.destroyAllWindows()
        
#shows video feed, ESC key kills program ^^
