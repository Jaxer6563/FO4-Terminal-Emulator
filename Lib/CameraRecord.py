# Python program to illustrate
# saving an operated video

# organize imports
import numpy as np
import cv2


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))






def recordCamera(name):
    while(True):
        ret, frame = cap.read() 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        out.write(frame)
        cv2.imshow('Original', frame)
        cv2.imshow('frame', hsv)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
