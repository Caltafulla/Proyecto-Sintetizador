#importar librerias y modulas para poder realizar las diferentes funciones

import sounddevice as sd
import numpy as np

class VCO:

    #Contructor de la clase VCO
    # numvco= Numero del VCO (Cual VCO es)
    # hzb= Frecuencia base del VCO
    # v= Volumen del VCO
    # onda= Tipo de onda (1. Seno, 2. Cuadrada, 3. Sierra)
    # wave= Funcion de la onda
    def __init__(self, volumenRL, num, onda = 0, hzb = 0):
        self.numvco = num
        self.hzb = hzb
        self.v = volumenRL
        self.onda = onda
        self.Wave = None

    #Metodo que nos devuelve cual sera la formula a utilizar dependiendo del tipo de onda
    def tona(self):
        if (self.onda == 1):
            self.Wave = Sine.generar
        elif (self.onda == 2):
            self.Wave = Square.generar
        elif (self.onda == 3):
            self.Wave = Saw.generar

    #Metodo para aumentar o disminuir el atributo semitonos del VCO dependiendo el parametro "semi"
    def addSemi(self, semi):
        if (self.hzb + semi <= 12 and self.hzb + semi >= -12):
            self.hzb = self.hzb + semi

    #Metodo para aumentar o disminuir el atributo "v" dependiendo del parametro "i"
    def volumen(self, i):
        if (self.v + i <= 100 and self.v + i >= 0):
            self.v = self.v + i

class Sine:
    #Devuelve un arreglo dependiendo al volumen del vco (v), al volumen general (volg) y la 
    #Frecuencia ingresada por parametros(hz)
    def generar(v, hz: int, volg):
        framerate = 44100
        time = 1000
        t =  np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = (volg/100) * ((v/100) * (np.sin(2 * np.pi * hz * t)))
        return wave


class Square:
    #Devuelve un arreglo dependiendo al volumen del vco (v), al volumen general (volg) y la 
    #Frecuencia ingresada por parametros(hz)
    def generar(v, hz: int, volg):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = (volg/100) * ((v/100) * ((11*(np.sin((2 * np.pi * hz * t))) + 3*(np.sin((2 * np.pi * hz * t)/(1/3))) + (14/10)*(np.sin((2 * np.pi * hz * t)/(1/5))) + (7/10)*(np.sin((2 * np.pi * hz * t)/(1/7))) + (15/100)*(np.sin((2 * np.pi * hz * t)/(1/9))))/(90/10)))
        return wave


class Saw:
    #Devuelve un arreglo dependiendo al volumen del vco (v), al volumen general (volg) y la 
    #Frecuencia ingresada por parametros(hz)
    def generar(v, hz: int, volg):
        framerate = 44100
        time = 1000
        t = np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = (volg/100) * ((v/100) * ((np.sin(2 * np.pi * hz * t) + (1/2)*np.sin(2 * np.pi * (hz*2) * t) + (1/3)*np.sin(2 * np.pi * (hz*3) * t) + (1/4)*np.sin(2 * np.pi * (hz*4) * t) + (1/5)*np.sin(2 * np.pi * (hz*5) * t))/(1 + (1/2))))
        return wave