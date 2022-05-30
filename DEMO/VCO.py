import sounddevice as sd
import numpy as np

class VCO:

    def __init__(self, valoro, timbre, volumenRL, onda ,hzb = 0):
        self.hzb = hzb
        self.vo = valoro
        self.timbre = timbre
        self.rl = volumenRL
        self.onda = onda
        self.f = None

    def tona(self):
        if (self.onda == 1):
            self.f = Sine.generar
        elif (self.onda == 2):
            self.f = Square.generar
        elif (self.onda == 3):
            self.f = Saw.generar

    def addSemi(self, semi):
        if (self.hzb + semi <= 12 and self.hzb + semi >= -12):
            self.hzb = self.hzb + semi

class Sine:
    def generar(hz: int):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = np.sin(2 * np.pi * hz * t)
        return wave


class Square:
    def generar(hz: int):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = ((11*(np.sin((2 * np.pi * hz * t))) + 3*(np.sin((2 * np.pi * hz * t)/(1/3))) + (14/10)*(np.sin((2 * np.pi * hz * t)/(1/5))) + (7/10)*(np.sin((2 * np.pi * hz * t)/(1/7))) + (15/100)*(np.sin((2 * np.pi * hz * t)/(1/9))))/(90/10))
        return wave


class Saw:
    def generar(hz: int):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = ((np.sin(2 * np.pi * hz * t) + (1/2)*np.sin(2 * np.pi * (hz*2) * t) + (1/3)*np.sin(2 * np.pi * (hz*3) * t) + (1/4)*np.sin(2 * np.pi * (hz*4) * t) + (1/5)*np.sin(2 * np.pi * (hz*5) * t))/(1 + (1/2)))
        return wave