import cv2
import numpy as np

def viewVideo(argument): # opens window with video playing, albiet without audio. Takes the filename as argument
    cap = cv2.VideoCapture(argument)
    if (cap.isOpened()==False):
        print('Error opening video file')
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow(argument, frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()