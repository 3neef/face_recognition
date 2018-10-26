import cv2
import numpy as np
import os
import subprocess as sp

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

with open(str(os.getcwd()+'/data.txt')) as f:
    su= sum(1 for _ in f)

cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(215,15,5),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id in range(1,100)):
                f=open(str(os.getcwd())+'/data.txt',"r")
                for line in (f):
                    if  Id== int(line.split('.')[0]):
                        Id=line.split('.')[1]
                        print line.split('.')[1]
                        if Id.isdigit()==True :
                        	Id = "unknown"
                        	print "unknown"

            else:
                print "0"
                Id="Unknown"
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
    cv2.imshow('im',im) 
    if cv2.waitKey(10) and 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
