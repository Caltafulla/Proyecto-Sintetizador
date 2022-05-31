import sounddevice as sd

class play():

    def __init__(self, volume, adsr):
        self.vol = volume
        self.adsr = adsr

    def GenerarSonido(wave):
        sd.play(wave, 44100)