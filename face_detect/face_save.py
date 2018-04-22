import cv2
import numpy as np
import sys

man_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap_device=cv2.VideoCapture(0)
while True:
    ret,img=cap_device.read()
    cv2.imshow('img',img)
    gray=cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)
    faces=man_face.detectMultiScale(gray,1.1,3)
    if len(faces)>1:
        for (x,y,w,h) in faces:
            cv2.rectangle (img,(x,y),(x+w,y+h),(222,0,0),3)
        cv2.imwrite('img.jpg',img)
        cap_device.release()
        cv2.destroyAllWindows ()
        sys.exit ()
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

