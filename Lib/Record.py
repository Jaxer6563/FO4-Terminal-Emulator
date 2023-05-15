from multiprocessing import Process
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import sys
import numpy as np
import cv2
rocket = 0
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))


def func1():
    global rocket
    print ('start func1')
    while rocket < sys.maxsize:
        rocket += 1
    print ('end func1')

def func2():
    global rocket
    print ('start func2')
    while rocket < sys.maxsize:
        rocket += 1
    print ('end func2')

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

def recordAux(name,length):
    
    freq = 44100
    duration = length
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write(name + '.wav', freq, recording)

if __name__!='__main__':
    p1 = Process(target=recordAux)
    p1.start()
    p2 = Process(target=recordCamera)
    p2.start()
    

    