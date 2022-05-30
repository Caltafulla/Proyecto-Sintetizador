import sounddevice as sd
from VCO import Sine, Square, Saw
import threading
import matplotlib.pyplot as plt

class SonidoP():
    def __init__(self, volume, adsr):
        self.vol = volume
        self.adsr = adsr

    def GenerarSonido(wave):
        sd.play(wave, 44100)
        sd.wait()

    def sonarO(wave):
        SonidoP.GenerarSonido(wave)

    def playN(sonarO, onda, hz, x):
        
        threads = []
        
        for VCO in onda:
            VCO.tona()
            if VCO.onda != 0:
                th = threading.Thread(target=lambda: sonarO(VCO.f(VCO.v, hz(VCO.hzb, x))))
                th.start()
                threads.append(th)

        for th in threads:
            th.join()