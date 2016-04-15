import numpy as np
import cv2

# If the CascadeClassifier file is not found, openCV actually does not issue anything.
# So be careful, must find the haar_dir and file correctly!
haar_dir = '/usr/local/Cellar/opencv/2.4.12/share/OpenCV/haarcascades/'
face_cascade = cv2.CascadeClassifier(haar_dir + 'haarcascade_frontalface_default.xml')


data_dir = '/Users/chengchenliu/Desktop/_work/data/'
cap = cv2.VideoCapture(data_dir + 'Video 1.avi')
i=0
ret, frame = cap.read()

#blahbalh

while(i<1800): #TODO: need to get the number of frames from cap

    i = i+1
    print i
    ret, frame = cap.read()

    #cv2.imshow('frame',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print "yes"
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Frame..',frame)
    print "no"

    c = cv2.waitKey(10)
    if(c==27): #exit if Esc is pressed
            break

cap.release()
cv2.destroyAllWindows()