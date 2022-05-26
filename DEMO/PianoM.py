class nota:
    def __init__(self, n, o):
        self.n = n
        self.o = o

class piano:
    def __init__(self, n, o):
        self.o = nota(n, o)

    def frecuencia(self):
        expo = (int(self.o.o) - 4) * 12 + int(self.o.n) - 10
        return 440 * (2 ** (1 / 12)) ** expo
