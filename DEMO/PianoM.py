class nota:
    def __init__(self, n, o):
        self.n = n
        self.o = o

class piano:
    o = []
    def __init__(self, ob = 0):
        for o in range (4, 6):
            for n in range (1, 13):
                self.o.append(nota(n, o))
        self.ob = ob

    def frecuencia(self, hzb, x):
        expo = (int(self.o[x].o) - 4 + self.ob) * 12 + int(self.o[x].n) - 10 + hzb
        return 440 * (2 ** (1 / 12)) ** expo

    def octavab (self, i):
        if (self.ob + i <= 1 and self.ob + i >= -1):
            self.ob = self.ob + i
