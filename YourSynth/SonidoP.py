import sounddevice as sd
from VCO import Sine, Square, Saw
import threading
import numpy as np

class SonidoP():

    def GenerarSonido(wave):
        sd.play(wave, 44100)
        sd.wait()

    def sonarO(wave):
        SonidoP.GenerarSonido(wave)

    def playN(sonarO, onda, hz, x, volg, brillo):
        threads = []
        temp =  0
        for VCO in onda:
            VCO.tona()
            if VCO.onda != 0:
                temp = temp + VCO.f(VCO.v, hz(VCO.hzb, x), volg)
                th = threading.Thread(target=lambda: sonarO(VCO.f(VCO.v, hz(VCO.hzb, x), volg)))
                th.start()
                threads.append(th)

        if (brillo):
            sonarO(temp)

        else:
            for th in threads:
                th.join()
