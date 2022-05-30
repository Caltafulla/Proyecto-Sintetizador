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
        #if (onda == 1):
        #    wave = Sine.generar(hz)
        #    SonidoP.GenerarSonido(wave)
        #elif (onda == 2):
        #    wave = Square.generar(hz)
        #    SonidoP.GenerarSonido(wave)
        #elif (onda == 3):
        #    wave = Saw.generar(hz)
        SonidoP.GenerarSonido(wave)

    def playN(sonarO, onda, hz, x):
        # 1
        threads = []
        
        for VCO in onda:
            VCO.tona()
            if VCO.onda != 0:
                plt.plot(VCO.f(VCO.v,hz(VCO.hzb, x))[:1000])
                plt.show()
                th = threading.Thread(target=lambda: sonarO(VCO.f(VCO.v, hz(VCO.hzb, x))))
                th.start()
                threads.append(th)
                
        # 2    
        for th in threads:
            th.join()