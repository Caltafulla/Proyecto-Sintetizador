class filter():

    #Consturctor que inicializa los aributos vol (volumen general) y brillo
    def __init__(self, vol = 50):
        self.vol = vol
        self.brillo = False

    #Metodo que aumenta o disminuye el atributo vol segun el parametro "i" ingresado
    def volgen(self, i):
        if (self.vol + i <= 100 and self.vol + i >= 0):
            self.vol = self.vol + i

    #Metodo para cambiar el estado de la variable brillo de true a false y viceversa
    def filterB(self):
        self.brillo = not(self.brillo)