import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import sys

'''
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
sd.wait()
write("recording0.wav", freq, recording)
'''
#sys.set _int_max_str_didg

def recordAux(name,length):
    
    freq = 44100
    duration = length
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write(name + '.wav', freq, recording)
    