import cv2
import numpy as np

vc = cv2.VideoCapture(0)

while -1:
    ret, img = vc.read()
    
    cv2.imshow('pyCam', img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        vc.release()
        cv2.destroyAllWindows()
        
