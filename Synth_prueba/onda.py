import numpy as np

class onda():

    def __init__(self, nombre):
        self.nombre = nombre

    def formula_onda(hz, nombre):
        # framerate = 44100
        # time = 1000
        # t = np.linspace(0, time/1000, int(framerate * time / 1000))
        # if (nombre == "Sine"):
            # wave = np.sin(2 * np.pi * hz * t)
            # return wave
        # elif (nombre == "Square"):
            # pass
        pass

class Sine(onda):

    def __init__(self):
        super().__init__("Sine")
    
    def generar(hz):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time/1000, int(framerate * time / 1000))
        return np.sin(2 * np.pi * hz * t)

class Square(onda):

    def __init__(self):
        super().__init__("Square")

    def generar(hz):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time/1000, int(framerate * time / 1000))
        return (11*(np.sin((2 * np.pi * hz * t))) + 3*(np.sin((2 * np.pi * hz * t)/(1/3))) + (14/10)*(np.sin((2 * np.pi * hz * t)/(1/5))) + (7/10)*(np.sin((2 * np.pi * hz * t)/(1/7))) + (15/100)*(np.sin((2 * np.pi * hz * t)/(1/9))))/(75/10) #Onda Cuadrada

class Saw ():
    def __init__(self):
        super().__init__("Square")

    def generar(hz):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time/1000, int(framerate * time / 1000))
        return (18*(np.sin(((2 * np.pi * t * hz)))) + 9*(np.sin((((2 * np.pi * t * hz)/2)))) + (61/10)*(np.sin((((2 * np.pi * t * hz)/3)))) + (45/10)*(np.sin((((2 * np.pi * t * hz)/4)))) + (36/10)*(np.sin((((2 * np.pi * t * hz)/5)))))/(1/1) #Onda Sierra