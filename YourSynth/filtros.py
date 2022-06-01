class filter():
    def __init__(self, vol = 50):
        self.vol = vol
        self.brillo = False

    def volgen(self, i):
        if (self.vol + i <= 100 and self.vol + i >= 0):
            self.vol = self.vol + i

    def filterB(self):
        self.brillo = not(self.brillo)