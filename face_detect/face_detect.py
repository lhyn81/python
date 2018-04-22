import cv2
import numpy as np

# man_face=cv2.CascadeClassifier('C:\\Users\\LH\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
man_face=cv2.CascadeClassifier('C:\\Users\\LH\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml')
# man_face=cv2.CascadeClassifier('C:\\Users\\LH\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
# man_face=cv2.CascadeClassifier('C:\\Users\\LH\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_smile.xml')
man_eye=cv2.CascadeClassifier ('haarcascade_eye.xml')
cap_device=cv2.VideoCapture(0)
while True:
    ret,img=cap_device.read()
    gray=cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)
    faces=man_face.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle (img,(x,y),(x+w,y+h),(222,0,0),3)
#         eye_gray=gray[y:y+h,x:x+h]
#         eye_color=img[y:y+h,x:x+h]
#         eyes=man_eye.detectMultiScale (eye_gray,1.3,3)
#         for(xx,yy,ww,hh) in eyes:
#             cv2.rectangle (eye_color,(xx,yy),(xx+ww,yy+hh),(0,222,0),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap_device.release()
cv2.destroyAllWindows ()
