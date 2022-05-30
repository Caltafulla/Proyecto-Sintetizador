class nota:
    def __init__(self, n, o):
        self.n = n
        self.o = o

class piano:
    o = []
    def __init__(self, ob = 0, hzb = 440, semitone = 0):
        for o in range (4, 6):
            for n in range (1, 13):
                self.o.append(nota(n, o))
        self.ob = ob
        self.hzb = hzb
        self.semitone = semitone

    def frecuencia(self, hzb, x):
        expo = (int(self.o[x].o) - 4 + self.ob) * 12 + int(self.o[x].n) - 10 + hzb
        return hzb * (2 ** (1 / 12)) ** expo

    def octavab (self, i):
        if (self.ob + i <= 1 and self.ob + i >= -1):
            self.ob = self.ob + i

    def hzbase(self, i):
        if (self.semitone + i <= 12 and self.semitone >= -12):
            self.semitone = self.semitone + i
            self.hzb = self.frecuencia(self.hzb, self.semitone)
