import cv2
import numpy as np
from twilio.rest import TwilioRestClient 
import time

#importing modules ^^

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

#importing cascade-classfier ^^

vc = cv2.VideoCapture(0)

#finding default camera ^^

while -1: 
    ret, img = vc.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.2, 2)
    
#converting img frame by frame to suitable type ^^

    for (x,y,w,h) in bodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,171),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") #account_sid, auth_token for twilio accaount.

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
