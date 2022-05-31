import sounddevice as sd
import numpy as np
import soundfile as sf

class grabadora():
    def __init__(self, framerate = 44100):
        self.framerate = framerate
        self.i = 0

    def recording(self, ndrray):
        file = sf.write(f"Prueba{self.i}.wav", ndrray, self.framerate)
        self.i = self.i + 1