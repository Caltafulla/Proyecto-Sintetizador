import sounddevice as sd
from VCO import Sine, Square, Saw
import threading

class SonidoP():
    def __init__(self, volume, adsr):
        self.vol = volume
        self.adsr = adsr

    def GenerarSonido(wave):
        sd.play(wave, 44100)

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

    def playN(sonarO, onda, hz):
        # 1
        threads = []
        
        for tipoO in onda:
            tipoO.tona()
            if tipoO.onda != 0:
                th = threading.Thread(target=lambda: sonarO(tipoO.f(hz)))
                th.start()
                threads.append(th)
                
        # 2    
        for th in threads:
            th.join()