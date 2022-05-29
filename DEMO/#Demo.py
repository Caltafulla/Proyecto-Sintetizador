#Demo
from tkinter import *
import tkinter
from turtle import width
from PIL import ImageTk, Image
from setuptools import Command
from SonidoP import SonidoP
from VCO import VCO
from PianoM import piano

sn = SonidoP.playN
ventana = tkinter.Tk()
#NOMBRE DE VENTANA
ventana.title("Synth")
vco1 = VCO(0, 0 ,0 ,0)
vco2 = VCO(0, 0 ,0 ,0)
vco3 = VCO(0, 0 ,0 ,0)
vcog = [vco1, vco2, vco3]

def asignar(num, vco):
    vco.onda = num

#FONDO
imagen = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Fondo_Mesa de trabajo 1 copia.png'))
label = tkinter.Label(image=imagen)
label.pack()

#CARGA BOTONES VCO/RESET
Sine = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-03.png'))
Square = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-04.png'))
Saw = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-05.png'))
SelectedSine = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-06.png'))
SelectedSquare = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-07.png'))
SelectedSaw = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-08.png'))
ResetBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Reload-09.png'))

#BOTONES VCO1

boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1))
boton1S.place(x = 226, y = 87, height = 70, width = 70)
boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1))
boton1Sq.place(x = 323, y = 87, height = 70, width = 70)
boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1))
boton1Sa.place(x = 420, y = 87, height = 70, width = 70)

#BOTONES VCO2
boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2))
boton2S.place(x = 226, y = 186, height = 70, width = 70)
boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2))
boton2Sq.place(x = 323, y = 186, height = 70, width = 70)
boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2))
boton2Sa.place(x = 420, y = 186, height = 70, width = 70)

#BOTONES VCO3
boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3))
boton3S.place(x = 226, y = 285, height = 70, width = 70)
boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3))
boton3Sq.place(x = 323, y = 285, height = 70, width = 70)
boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3))
boton3Sa.place(x = 420, y = 285, height = 70, width = 70)

#BOTONES RESET
Rset1 = tkinter.Button(image = ResetBtt, relief = FLAT, borderwidth = 0)
Rset1.place(x = 12, y = 107, height = 33, width = 33)

#BOTONES PIANO

#OCTAVA 1
Do1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(1, 4).frecuencia()))
Do1.place(x = 115, y = 430, height = 250, width = 50)
Re1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(3, 4).frecuencia()))
Re1.place(x = 165, y = 430, height = 250, width = 50)
Mi1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(5, 4).frecuencia()))
Mi1.place(x = 215, y = 430, height = 250, width = 50)
Fa1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(6, 4).frecuencia()))
Fa1.place(x = 265, y = 430, height = 250, width = 50)
Sol1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(8, 4).frecuencia()))
Sol1.place(x = 315, y = 430, height = 250, width = 50)
La1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(10, 4).frecuencia()))
La1.place(x = 365, y = 430, height = 250, width = 50)
Si1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(12, 4).frecuencia()))
Si1.place(x = 415, y = 430, height = 250, width = 50)

#OCTAVA 2
Do2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(13, 4).frecuencia()))
Do2.place(x = 465, y = 430, height = 250, width = 50)
Re2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(15, 4).frecuencia()))
Re2.place(x = 515, y = 430, height = 250, width = 50)
Mi2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(17, 4).frecuencia()))
Mi2.place(x = 565, y = 430, height = 250, width = 50)
Fa2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(18, 4).frecuencia()))
Fa2.place(x = 615, y = 430, height = 250, width = 50)
Sol2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(20, 4).frecuencia()))
Sol2.place(x = 665, y = 430, height = 250, width = 50)
La2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(22, 4).frecuencia()))
La2.place(x = 715, y = 430, height = 250, width = 50)
Si2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(24, 4).frecuencia()))
Si2.place(x = 765, y = 430, height = 250, width = 50)
Do3 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(25, 4).frecuencia()))
Do3.place(x = 815, y = 430, height = 250, width = 50)

#NEGRAS
#OCTAVA 1
DoS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(2, 4).frecuencia()), bg ="black")
DoS1.place(x = 150, y = 430, height = 150, width = 30)
ReS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(4, 4).frecuencia()), bg ="black")
ReS1.place(x = 200, y = 430, height = 150, width = 30)
FaS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(7, 4).frecuencia()), bg ="black")
FaS1.place(x = 300, y = 430, height = 150, width = 30)
SolS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(9, 4).frecuencia()), bg ="black")
SolS1.place(x = 350, y = 430, height = 150, width = 30)
LaS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(11, 4).frecuencia()), bg ="black")
LaS1.place(x = 400, y = 430, height = 150, width = 30)

#OCTAVA 2
DoS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(14, 4).frecuencia()), bg ="black")
DoS2.place(x = 500, y = 430, height = 150, width = 30)
ReS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(16, 4).frecuencia()), bg ="black")
ReS2.place(x = 550, y = 430, height = 150, width = 30)
FaS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(19, 4).frecuencia()), bg ="black")
FaS2.place(x = 650, y = 430, height = 150, width = 30)
SolS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(21, 4).frecuencia()), bg ="black")
SolS2.place(x = 700, y = 430, height = 150, width = 30)
LaS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano(23, 4).frecuencia()), bg ="black")
LaS2.place(x = 750, y = 430, height = 150, width = 30)
ventana.mainloop()
