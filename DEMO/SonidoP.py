import sounddevice as sd
from VCO import Sine, Square, Saw
import threading
from grabadora import grabadora

class SonidoP():

    def GenerarSonido(wave):
        sd.play(wave, 44100)
        sd.wait()

    def sonarO(wave):
        SonidoP.GenerarSonido(wave)

    def playN(sonarO, onda, hz, x, volg):
        threads = []
        g = grabadora()
        for VCO in onda:
            VCO.tona()
            if VCO.onda != 0:
                g.recording(VCO.f(VCO.v, hz(VCO.hzb, x), volg))
                th = threading.Thread(target=lambda: sonarO(VCO.f(VCO.v, hz(VCO.hzb, x), volg)))
                th.start()
                threads.append(th)

        for th in threads:
            th.join()
