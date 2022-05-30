#Demo
from tkinter import *
import tkinter
from turtle import width
from PIL import ImageTk, Image
from setuptools import Command
from SonidoP import SonidoP
from VCO import VCO
from PianoM import piano as p

piano = p()

sn = SonidoP.playN
ventana = tkinter.Tk()
#NOMBRE DE VENTANA
ventana.title("Synth")
vco1 = VCO(0, 0 ,50 ,0)
vco2 = VCO(0, 0 ,50 ,0)
vco3 = VCO(0, 0 ,50 ,0)
vcog = [vco1, vco2, vco3]

def asignar(num, vco, numind):
    vco.onda = num
    if (numind == 1):
        boton1S = tkinter.Button(image = SelectedSine, command= lambda: asignar(1, vco1,1), relief = FLAT)
        boton1S.place(x = 226, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1,2), relief = FLAT)
        boton1Sq.place(x = 323, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1,3), relief = FLAT)
        boton1Sa.place(x = 420, y = 87, height = 70, width = 70)
    elif (numind ==2):
        boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1,1), relief = FLAT)
        boton1S.place(x = 226, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = SelectedSquare, command= lambda: asignar(2, vco1,2), relief = FLAT)
        boton1Sq.place(x = 323, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1,3), relief = FLAT)
        boton1Sa.place(x = 420, y = 87, height = 70, width = 70)
    elif (numind ==3):
        boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1,1), relief = FLAT)
        boton1S.place(x = 226, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1,2), relief = FLAT)
        boton1Sq.place(x = 323, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = SelectedSaw, command= lambda: asignar(3, vco1,3), relief = FLAT)
        boton1Sa.place(x = 420, y = 87, height = 70, width = 70)
    elif (numind ==4):
        boton2S = tkinter.Button(image = SelectedSine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 226, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 323, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 420, y = 186, height = 70, width = 70)
    elif (numind ==5):
        boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 226, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = SelectedSquare, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 323, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 420, y = 186, height = 70, width = 70)
    elif (numind ==6):
        boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 226, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 323, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = SelectedSaw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 420, y = 186, height = 70, width = 70)
    elif (numind ==7):
        boton3S = tkinter.Button(image = SelectedSine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 226, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 323, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 420, y = 285, height = 70, width = 70)
    elif (numind ==8):
        boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 226, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = SelectedSquare, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 323, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 420, y = 285, height = 70, width = 70)
    elif (numind ==9):
        boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 226, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 323, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = SelectedSaw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 420, y = 285, height = 70, width = 70)
        
def reset(nmvco):
    if(nmvco == 1):
        boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1, 1), relief = FLAT)
        boton1S.place(x = 226, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1, 2), relief = FLAT)
        boton1Sq.place(x = 323, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1, 3), relief = FLAT)
        boton1Sa.place(x = 420, y = 87, height = 70, width = 70)
        vco1.onda = 0
    elif (nmvco == 2):
        boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 226, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 323, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 420, y = 186, height = 70, width = 70)
        vco2.onda = 0
    elif (nmvco == 3):
        boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 226, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 323, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 420, y = 285, height = 70, width = 70)
        vco3.onda = 0

def actv(vco, i):
    vco.volumen(i)
    labelvco1V = tkinter.Label(text = vco1.v, bg= "black", fg= "white")
    labelvco1V.place(x = 778, y = 97)

#FONDO
imagen = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Fondo_Mesa de trabajo 1 copia.png'))
label = tkinter.Label(image=imagen)
label.pack()

#Lables Volumen
labelvco1V = tkinter.Label(text = vco1.v, bg= "black", fg= "white")
labelvco1V.place(x = 778, y = 97)

#CARGA BOTONES VCO/RESET/VOLUME+-/OCTAVA
Sine = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-03.png'))
Square = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-04.png'))
Saw = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-05.png'))
SelectedSine = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-06.png'))
SelectedSquare = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-07.png'))
SelectedSaw = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-08.png'))
ResetBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Reload-09.png'))
MásBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomeno-18.png'))
MenosBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomeno-17.png'))
MásBttbig = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomenobig-19.png'))
MenosBttbig = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomenobig-20.png'))

#BOTONES VCO1

boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1, 1), relief = FLAT)
boton1S.place(x = 270, y = 87, height = 70, width = 70)
boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1, 2), relief = FLAT)
boton1Sq.place(x = 367, y = 87, height = 70, width = 70)
boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1, 3), relief = FLAT)
boton1Sa.place(x = 464, y = 87, height = 70, width = 70)

#BOTONES VCO2
boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
boton2S.place(x = 270, y = 186, height = 70, width = 70)
boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
boton2Sq.place(x = 367, y = 186, height = 70, width = 70)
boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
boton2Sa.place(x = 464, y = 186, height = 70, width = 70)

#BOTONES VCO3
boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
boton3S.place(x = 270, y = 285, height = 70, width = 70)
boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
boton3Sq.place(x = 367, y = 285, height = 70, width = 70)
boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
boton3Sa.place(x = 464, y = 285, height = 70, width = 70)

#BOTONES RESET
Rset1 = tkinter.Button(image = ResetBtt, command = lambda: reset(1), relief = FLAT, borderwidth = 0)
Rset1.place(x = 35, y = 107, height = 33, width = 33)
Rset2 = tkinter.Button(image = ResetBtt, command = lambda: reset(2), relief = FLAT, borderwidth = 0)
Rset2.place(x = 35, y = 206, height = 33, width = 33)
Rset3 = tkinter.Button(image = ResetBtt, command = lambda: reset(3), relief = FLAT, borderwidth = 0)
Rset3.place(x = 35, y = 305, height = 33, width = 33)

#BOTONES VOLUMEN / TONO

#VCO1
VolumemsVCO1 = tkinter.Button(image = MenosBtt, comman = lambda: actv(vco1, 5), relief = FLAT, borderwidth = 0)
VolumemsVCO1.place(x = 868, y = 91, height = 26, width = 26)
VolumemnVCO1 = tkinter.Button(image = MásBtt, comman = lambda: actv(vco1, -5), relief = FLAT, borderwidth = 0)
VolumemnVCO1.place(x = 673, y = 91, height = 26, width = 26)
TonemsVCO1 = tkinter.Button(image = MenosBtt, command = lambda: vco1.addSemi(1),relief = FLAT, borderwidth = 0)
TonemsVCO1.place(x = 868, y = 131, height = 26, width = 26)
TonemnVCO1 = tkinter.Button(image = MásBtt, command = lambda: vco1.addSemi(-1), relief = FLAT, borderwidth = 0)
TonemnVCO1.place(x = 673, y = 131, height = 26, width = 26)

#VCO2
VolumemsVCO2 = tkinter.Button(image = MenosBtt, comman = lambda: vco2.volumen(5), relief = FLAT, borderwidth = 0)
VolumemsVCO2.place(x = 868, y = 190, height = 26, width = 26)
VolumemnVCO2 = tkinter.Button(image = MásBtt, comman = lambda: vco2.volumen(-5), relief = FLAT, borderwidth = 0)
VolumemnVCO2.place(x = 673, y = 190, height = 26, width = 26)
TonemsVCO2 = tkinter.Button(image = MenosBtt, command = lambda: vco2.addSemi(1), relief = FLAT, borderwidth = 0)
TonemsVCO2.place(x = 868, y = 230, height = 26, width = 26)
TonemnVCO2 = tkinter.Button(image = MásBtt, command = lambda: vco2.addSemi(-1), relief = FLAT, borderwidth = 0)
TonemnVCO2.place(x = 673, y = 230, height = 26, width = 26)

#VCO3
VolumemsVCO3 = tkinter.Button(image = MenosBtt, comman = lambda: vco3.volumen(5), relief = FLAT, borderwidth = 0)
VolumemsVCO3.place(x = 868, y = 289, height = 26, width = 26)
VolumemnVCO3 = tkinter.Button(image = MásBtt, command = lambda: vco3.volumen(-5), relief = FLAT, borderwidth = 0)
VolumemnVCO3.place(x = 673, y = 289, height = 26, width = 26)
TonemsVCO3 = tkinter.Button(image = MenosBtt, command = lambda: vco3.addSemi(1), relief = FLAT, borderwidth = 0)
TonemsVCO3.place(x = 868, y = 329, height = 26, width = 26)
TonemnVCO3 = tkinter.Button(image = MásBtt, command = lambda: vco3.addSemi(-1), relief = FLAT, borderwidth = 0)
TonemnVCO3.place(x = 673, y = 329, height = 26, width = 26)

#BOTONES OCTAVA ACTUAL
Aumento = tkinter.Button(image = MásBttbig, command= lambda: piano.octavab(1), relief = FLAT, borderwidth = 0)
Aumento.place(x = 75, y = 502, height = 37, width = 37)
Dismin = tkinter.Button(image = MenosBttbig, command= lambda: piano.octavab(-1), relief = FLAT, borderwidth = 0)
Dismin.place(x = 75, y = 622, height = 37, width = 37)

#BOTONES PIANO
#OCTAVA 1
Do1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 0))
Do1.place(x = 200, y = 430, height = 250, width = 50)
Re1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 2))
Re1.place(x = 250, y = 430, height = 250, width = 50)
Mi1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 4))
Mi1.place(x = 300, y = 430, height = 250, width = 50)
Fa1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 5))
Fa1.place(x = 350, y = 430, height = 250, width = 50)
Sol1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 7))
Sol1.place(x = 400, y = 430, height = 250, width = 50)
La1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 9))
La1.place(x = 450, y = 430, height = 250, width = 50)
Si1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 11))
Si1.place(x = 500, y = 430, height = 250, width = 50)

#OCTAVA 2
Do2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 12))
Do2.place(x = 550, y = 430, height = 250, width = 50)
Re2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 14))
Re2.place(x = 600, y = 430, height = 250, width = 50)
Mi2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 16))
Mi2.place(x = 650, y = 430, height = 250, width = 50)
Fa2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 17))
Fa2.place(x = 700, y = 430, height = 250, width = 50)
Sol2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 19))
Sol2.place(x = 750, y = 430, height = 250, width = 50)
La2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 21))
La2.place(x = 800, y = 430, height = 250, width = 50)
Si2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 23))
Si2.place(x = 850, y = 430, height = 250, width = 50)

#NEGRAS
#OCTAVA 1
DoS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 1), bg ="black")
DoS1.place(x = 235, y = 430, height = 150, width = 30)
ReS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 3), bg ="black")
ReS1.place(x = 285, y = 430, height = 150, width = 30)
FaS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 6), bg ="black")
FaS1.place(x = 385, y = 430, height = 150, width = 30)
SolS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 8), bg ="black")
SolS1.place(x = 435, y = 430, height = 150, width = 30)
LaS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 10), bg ="black")
LaS1.place(x = 485, y = 430, height = 150, width = 30)

#OCTAVA 2
DoS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 13), bg ="black")
DoS2.place(x = 585, y = 430, height = 150, width = 30)
ReS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 15), bg ="black")
ReS2.place(x = 635, y = 430, height = 150, width = 30)
FaS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 18), bg ="black")
FaS2.place(x = 735, y = 430, height = 150, width = 30)
SolS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 20), bg ="black")
SolS2.place(x = 785, y = 430, height = 150, width = 30)
LaS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 22), bg ="black")
LaS2.place(x = 835, y = 430, height = 150, width = 30)
ventana.mainloop()
