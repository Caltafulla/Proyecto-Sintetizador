#importar librerias y modulas para poder realizar las diferentes funciones

import sounddevice as sd
from VCO import Sine, Square, Saw
import threading
import numpy as np

class SonidoP():

    #Metodo para reproducir un sonido segun el arreglo pasado como parametro
    #En este caso el arreglo son los diferentes valores que puede tomar la onda en el tiempo
    def GenerarSonido(wave):
        sd.play(wave, 44100)
        sd.wait()

    #Metodo que llama a la funcion GenerarSonido
    def sonarO(wave):
        SonidoP.GenerarSonido(wave)

    #Metodo para hacer sonar varios VCO al mismo tiempo
    def playN(sonarO, onda, hz, x, volg, brillo):
        threads = []
        temp =  0
        #Ciclo que recorre todos los VCO que estan en el vector "onda"
        for VCO in onda:
            VCO.tona()
            if VCO.onda != 0:
                #Suma de las ondas
                temp = temp + VCO.Wave(VCO.v, hz(VCO.hzb, x), volg)
                #Se agregan las funciones de generar y reproducir el sonido para reproducirlas 
                #En hilos y hacer que suenen simultaneamente
                th = threading.Thread(target=lambda: sonarO(VCO.Wave(VCO.v, hz(VCO.hzb, x), volg)))
                th.start()
                threads.append(th)

        #Si se tiene activada la funcion brillo, reproducira la onda superpuesta
        #Y si no la funcion en simultaneo trabajando por hilos
        if (brillo):
            sonarO(temp)
        else:
            for th in threads:
                th.join()
