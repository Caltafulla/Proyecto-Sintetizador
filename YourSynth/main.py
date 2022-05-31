#Demo
from tarfile import REGULAR_TYPES
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
#NOMBRE DE VENTANA.
ventana.title("Synth")
vco1 = VCO(0, 0 ,50 ,0, 1)
vco2 = VCO(0, 0 ,50 ,0, 2)
vco3 = VCO(0, 0 ,50 ,0, 3)
vcog = [vco1, vco2, vco3]

#CARGA IMAGENES DE BOTONES 
Sine = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-03.png'))
Square = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-04.png'))
Saw = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Synth-05.png'))
SelectedSine = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-06.png'))
SelectedSquare = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-07.png'))
SelectedSaw = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\SynthSelected-08.png'))
ResetBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Reload-09.png'))
MásBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomeno-17.png'))
MenosBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomeno-18.png'))
DMásBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\darkmaomeno-17.png'))
DMenosBtt = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\darkmaomeno-18.png'))
DLabelPl = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Darklblplc-21.png'))
MásBttbig = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomenobig-19.png'))
MenosBttbig = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\maomenobig-20.png'))
imagenv = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\lblplc-21.png'))
imagenTT = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\OctvLabel-22.png'))
RecordB = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Record-11.png'))
RecordS = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Record-12.png'))
PlayB = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Play-13.png'))
PlayG = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Play-14.png'))
PauseB = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Pause-16.png'))
PauseG = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Pause-15.png'))

def asignar(num, vco, numind):
    vco.onda = num
    if (numind == 1):
        boton1S = tkinter.Button(image = SelectedSine, command= lambda: asignar(1, vco1,1), relief = FLAT)
        boton1S.place(x = 270, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1,2), relief = FLAT)
        boton1Sq.place(x = 367, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1,3), relief = FLAT)
        boton1Sa.place(x = 464, y = 87, height = 70, width = 70)
    elif (numind ==2):
        boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1,1), relief = FLAT)
        boton1S.place(x = 270, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = SelectedSquare, command= lambda: asignar(2, vco1,2), relief = FLAT)
        boton1Sq.place(x = 367, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1,3), relief = FLAT)
        boton1Sa.place(x = 464, y = 87, height = 70, width = 70)
    elif (numind ==3):
        boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1,1), relief = FLAT)
        boton1S.place(x = 270, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1,2), relief = FLAT)
        boton1Sq.place(x = 367, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = SelectedSaw, command= lambda: asignar(3, vco1,3), relief = FLAT)
        boton1Sa.place(x = 464, y = 87, height = 70, width = 70)
    elif (numind ==4):
        boton2S = tkinter.Button(image = SelectedSine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 270, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 367, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 464, y = 186, height = 70, width = 70)
    elif (numind ==5):
        boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 270, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = SelectedSquare, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 367, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 464, y = 186, height = 70, width = 70)
    elif (numind ==6):
        boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 270, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 367, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = SelectedSaw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 464, y = 186, height = 70, width = 70)
    elif (numind ==7):
        boton3S = tkinter.Button(image = SelectedSine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 270, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 367, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 464, y = 285, height = 70, width = 70)
    elif (numind ==8):
        boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 270, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = SelectedSquare, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 367, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 464, y = 285, height = 70, width = 70)
    elif (numind ==9):
        boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 270, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 367, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = SelectedSaw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 464, y = 285, height = 70, width = 70)
        
def reset(nmvco):
    if(nmvco == 1):
        boton1S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco1, 1), relief = FLAT)
        boton1S.place(x = 270, y = 87, height = 70, width = 70)
        boton1Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco1, 2), relief = FLAT)
        boton1Sq.place(x = 367, y = 87, height = 70, width = 70)
        boton1Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco1, 3), relief = FLAT)
        boton1Sa.place(x = 464, y = 87, height = 70, width = 70)
        vco1.onda = 0
    elif (nmvco == 2):
        boton2S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco2,4), relief = FLAT)
        boton2S.place(x = 270, y = 186, height = 70, width = 70)
        boton2Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco2,5), relief = FLAT)
        boton2Sq.place(x = 367, y = 186, height = 70, width = 70)
        boton2Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco2,6), relief = FLAT)
        boton2Sa.place(x = 464, y = 186, height = 70, width = 70)
        vco2.onda = 0
    elif (nmvco == 3):
        boton3S = tkinter.Button(image = Sine, command= lambda: asignar(1, vco3,7), relief = FLAT)
        boton3S.place(x = 270, y = 285, height = 70, width = 70)
        boton3Sq = tkinter.Button(image = Square, command= lambda: asignar(2, vco3,8), relief = FLAT)
        boton3Sq.place(x = 367, y = 285, height = 70, width = 70)
        boton3Sa = tkinter.Button(image = Saw, command= lambda: asignar(3, vco3,9), relief = FLAT)
        boton3Sa.place(x = 464, y = 285, height = 70, width = 70)
        vco3.onda = 0

def actv(vco, i):
    vco.volumen(i)
    if (vco.numvco == 1):
        labelv1 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
        labelv1.place(x = 732, y = 89)
        labelvco1V = tkinter.Label(text = vco1.v, bg= "#141414", fg= "white")
        labelvco1V.place(x = 778, y = 94)
    elif (vco.numvco == 2):
        labelv2 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
        labelv2.place(x = 732, y = 188)
        labelvco2V = tkinter.Label(text = vco2.v, bg= "#141414", fg= "white")
        labelvco2V.place(x = 778, y = 194)
    elif (vco.numvco == 3):
        labelv3 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
        labelv3.place(x = 732, y = 287)
        labelvco3V = tkinter.Label(text = vco3.v, bg= "#141414", fg= "white")
        labelvco3V.place(x = 778, y = 293)

def actt(vco, i):
    vco.addSemi(i)
    if (vco.numvco == 1):
        labetn1 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
        labetn1.place(x = 732, y = 129)
        labelvco1T = tkinter.Label(text = vco1.hzb, bg= "#141414", fg= "white")
        labelvco1T.place(x = 778, y = 135)
    elif (vco.numvco == 2):
        labetn2 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
        labetn2.place(x = 732, y = 228)
        labelvco2T = tkinter.Label(text = vco2.hzb, bg= "#141414", fg= "white")
        labelvco2T.place(x = 778, y = 234)
    elif (vco.numvco == 3):
        labetn3 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
        labetn3.place(x = 732, y = 327)
        labelvco3T = tkinter.Label(text = vco3.hzb, bg= "#141414", fg= "white")
        labelvco3T.place(x = 778, y = 333)

def actO(piano, i):
    piano.octavab(i)
    if (piano.ob >= -1 and piano.ob <= 1):
        labelocT = tkinter.Label(image= imagenTT, relief = FLAT, borderwidth = 0)
        labelocT.place(x = 60, y = 562)
        OcvtLbl = tkinter.Label(text = piano.ob, bg= "#141414", fg= "white")
        OcvtLbl.place(x = (92), y = 567)

def actvG(piano, i):
    piano.volgen(i)
    if (piano.vol >= 0 and piano.vol <= 100):
        LblGVol = tkinter.Label(image= DLabelPl, relief = FLAT, borderwidth = 0)
        LblGVol.place(x = 516, y = 8)
        LblGVolT = tkinter.Label(text = piano.vol, bg= "#141414", fg= "white")
        LblGVolT.place(x = 563, y = 11)

def acttG(piano, i):
    piano.hzbase(i)
    if (piano.semitone <= 12 and piano.semitone >= -12):
        LblGTone = tkinter.Label(image= DLabelPl, relief = FLAT, borderwidth = 0)
        LblGTone.place(x = 811, y = 8)
        LblGToneT = tkinter.Label(text = piano.semitone, bg= "#141414", fg= "white")
        LblGToneT.place(x = 858, y = 11)

#FONDO
imagen = ImageTk.PhotoImage(Image.open(r'DEMO\ImageSources\Fondo_Mesa de trabajo 1 copia.png'))
label = tkinter.Label(image=imagen)
label.pack()

#BOTONES DE CONTROL DE REPRODUCCIÓN
InitRec = tkinter.Button(image= RecordB, relief = FLAT, borderwidth = 0)
InitRec.place(x = 60, y = 10, height = 21, width = 21)
InitPlay = tkinter.Button(image= PlayB, relief = FLAT, borderwidth = 0)
InitPlay.place(x = 90, y = 10, height = 21, width = 21)
InitPause = tkinter.Button(image= PauseB, relief = FLAT, borderwidth = 0)
InitPause.place(x = 120, y = 10, height = 21, width = 21)

#Lables Volumen
#VCO1
labelv1 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
labelv1.place(x = 732, y = 89)
labelvco1V = tkinter.Label(text = vco1.v, bg= "#141414", fg= "white")
labelvco1V.place(x = 778, y = 94)
#VCO2
labelv2 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
labelv2.place(x = 732, y = 188)
labelvco2V = tkinter.Label(text = vco2.v, bg= "#141414", fg= "white")
labelvco2V.place(x = 778, y = 194)
#VCO3
labelv3 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
labelv3.place(x = 732, y = 287)
labelvco3V = tkinter.Label(text = vco3.v, bg= "#141414", fg= "white")
labelvco3V.place(x = 778, y = 293)

#Labels Tono 
#VCO1
labetn1 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
labetn1.place(x = 732, y = 129)
labelvco1T = tkinter.Label(text = vco1.hzb, bg= "#141414", fg= "white")
labelvco1T.place(x = 778, y = 135)
#VCO2
labetn2 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
labetn2.place(x = 732, y = 228)
labelvco2T = tkinter.Label(text = vco2.hzb, bg= "#141414", fg= "white")
labelvco2T.place(x = 778, y = 234)
#VCO3
labetn3 = tkinter.Label(image= imagenv, relief = FLAT, borderwidth = 0)
labetn3.place(x = 732, y = 327)
labelvco3T = tkinter.Label(text = vco3.hzb, bg= "#141414", fg= "white")
labelvco3T.place(x = 778, y = 333)

#VOLUMEN/TONO GENERAL

#VOLUMEN
LblGVol = tkinter.Label(image= DLabelPl, relief = FLAT, borderwidth = 0)
LblGVol.place(x = 516, y = 8)
MnGVol = tkinter.Button(image= DMenosBtt, command= lambda: actvG(piano, -1), relief = FLAT, borderwidth = 0)
MnGVol.place(x = 480, y = 10, height = 26, width = 26)
MsGVol = tkinter.Button(image= DMásBtt, command= lambda: actvG(piano, 1), relief = FLAT, borderwidth = 0)
MsGVol.place(x = 636, y = 10, height = 26, width = 26)
LblGVolT = tkinter.Label(text = piano.vol, bg= "#141414", fg= "white")
LblGVolT.place(x = 563, y = 11)

#TONO
LblGTone = tkinter.Label(image= DLabelPl, relief = FLAT, borderwidth = 0)
LblGTone.place(x = 811, y = 8)
MnGTone = tkinter.Button(image= DMenosBtt, command= lambda: acttG(piano, -1), relief = FLAT, borderwidth = 0)
MnGTone.place(x = 775, y = 10, height = 26, width = 26)
MsGTone = tkinter.Button(image= DMásBtt, command= lambda: acttG(piano, 1), relief = FLAT, borderwidth = 0)
MsGTone.place(x = 931, y = 10, height = 26, width = 26)
LblGToneT = tkinter.Label(text = piano.ob, bg= "#141414", fg= "white")
LblGToneT.place(x = 858, y = 11)

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
VolumemsVCO1 = tkinter.Button(image = MásBtt, comman = lambda: actv(vco1, 5), relief = FLAT, borderwidth = 0)
VolumemsVCO1.place(x = 850, y = 91, height = 26, width = 26)
VolumemnVCO1 = tkinter.Button(image = MenosBtt, comman = lambda: actv(vco1, -5), relief = FLAT, borderwidth = 0)
VolumemnVCO1.place(x = 700, y = 91, height = 26, width = 26)
TonemsVCO1 = tkinter.Button(image = MásBtt, command = lambda: actt(vco1, 1),relief = FLAT, borderwidth = 0)
TonemsVCO1.place(x = 850, y = 131, height = 26, width = 26)
TonemnVCO1 = tkinter.Button(image = MenosBtt, command = lambda: actt(vco1, -1), relief = FLAT, borderwidth = 0)
TonemnVCO1.place(x = 700, y = 131, height = 26, width = 26)

#VCO2
VolumemsVCO2 = tkinter.Button(image = MásBtt, comman = lambda: actv(vco2, 5), relief = FLAT, borderwidth = 0)
VolumemsVCO2.place(x = 850, y = 190, height = 26, width = 26)
VolumemnVCO2 = tkinter.Button(image = MenosBtt, comman = lambda: actv(vco2, -5), relief = FLAT, borderwidth = 0)
VolumemnVCO2.place(x = 700, y = 190, height = 26, width = 26)
TonemsVCO2 = tkinter.Button(image = MásBtt, command = lambda: actt(vco2, 1), relief = FLAT, borderwidth = 0)
TonemsVCO2.place(x = 850, y = 230, height = 26, width = 26)
TonemnVCO2 = tkinter.Button(image = MenosBtt, command = lambda: actt(vco2, -1), relief = FLAT, borderwidth = 0)
TonemnVCO2.place(x = 700, y = 230, height = 26, width = 26)

#VCO3
VolumemsVCO3 = tkinter.Button(image = MásBtt, comman = lambda: actv(vco3, 5), relief = FLAT, borderwidth = 0)
VolumemsVCO3.place(x = 850, y = 289, height = 26, width = 26)
VolumemnVCO3 = tkinter.Button(image = MenosBtt, command = lambda: actv(vco3, -5), relief = FLAT, borderwidth = 0)
VolumemnVCO3.place(x = 700, y = 289, height = 26, width = 26)
TonemsVCO3 = tkinter.Button(image = MásBtt, command = lambda: actt(vco3, 1), relief = FLAT, borderwidth = 0)
TonemsVCO3.place(x = 850, y = 329, height = 26, width = 26)
TonemnVCO3 = tkinter.Button(image = MenosBtt, command = lambda: actt(vco3, -1), relief = FLAT, borderwidth = 0)
TonemnVCO3.place(x = 700, y = 329, height = 26, width = 26)

#BOTONES OCTAVA ACTUAL
labelocT = tkinter.Label(image= imagenTT, relief = FLAT, borderwidth = 0)
labelocT.place(x = 60, y = 562)
Aumento = tkinter.Button(image = MásBttbig, command= lambda: actO(piano, 1), relief = FLAT, borderwidth = 0)
Aumento.place(x = (81.5), y = 510, height = 37, width = 37)
Dismin = tkinter.Button(image = MenosBttbig, command= lambda: actO(piano, -1), relief = FLAT, borderwidth = 0)
Dismin.place(x = (81.5), y = 610, height = 37, width = 37)
OcvtLbl = tkinter.Label(text = piano.ob, bg= "#141414", fg= "white")
OcvtLbl.place(x = (92), y = 567)

#BOTONES PIANO
#OCTAVA 1
Do1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 0, piano.vol, piano.brillo))
Do1.place(x = 200, y = 430, height = 250, width = 50)
Re1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 2, piano.vol, piano.brillo))
Re1.place(x = 250, y = 430, height = 250, width = 50)
Mi1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 4, piano.vol, piano.brillo))
Mi1.place(x = 300, y = 430, height = 250, width = 50)
Fa1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 5, piano.vol, piano.brillo))
Fa1.place(x = 350, y = 430, height = 250, width = 50)
Sol1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 7, piano.vol, piano.brillo))
Sol1.place(x = 400, y = 430, height = 250, width = 50)
La1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 9, piano.vol, piano.brillo))
La1.place(x = 450, y = 430, height = 250, width = 50)
Si1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 11, piano.vol, piano.brillo))
Si1.place(x = 500, y = 430, height = 250, width = 50)

#OCTAVA 2
Do2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 12, piano.vol))
Do2.place(x = 550, y = 430, height = 250, width = 50)
Re2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 14, piano.vol))
Re2.place(x = 600, y = 430, height = 250, width = 50)
Mi2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 16, piano.vol))
Mi2.place(x = 650, y = 430, height = 250, width = 50)
Fa2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 17, piano.vol))
Fa2.place(x = 700, y = 430, height = 250, width = 50)
Sol2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 19, piano.vol))
Sol2.place(x = 750, y = 430, height = 250, width = 50)
La2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 21, piano.vol))
La2.place(x = 800, y = 430, height = 250, width = 50)
Si2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 23, piano.vol))
Si2.place(x = 850, y = 430, height = 250, width = 50)

#NEGRAS
#OCTAVA 1
DoS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 1, piano.vol), bg ="black")
DoS1.place(x = 235, y = 430, height = 150, width = 30)
ReS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 3, piano.vol), bg ="black")
ReS1.place(x = 285, y = 430, height = 150, width = 30)
FaS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 6, piano.vol), bg ="black")
FaS1.place(x = 385, y = 430, height = 150, width = 30)
SolS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 8, piano.vol), bg ="black")
SolS1.place(x = 435, y = 430, height = 150, width = 30)
LaS1 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 10, piano.vol), bg ="black")
LaS1.place(x = 485, y = 430, height = 150, width = 30)

#OCTAVA 2
DoS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 13, piano.vol), bg ="black")
DoS2.place(x = 585, y = 430, height = 150, width = 30)
ReS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 15, piano.vol), bg ="black")
ReS2.place(x = 635, y = 430, height = 150, width = 30)
FaS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 18, piano.vol), bg ="black")
FaS2.place(x = 735, y = 430, height = 150, width = 30)
SolS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 20, piano.vol), bg ="black")
SolS2.place(x = 785, y = 430, height = 150, width = 30)
LaS2 = tkinter.Button(ventana, command= lambda: sn(SonidoP.sonarO, vcog, piano.frecuencia, 22, piano.vol), bg ="black")
LaS2.place(x = 835, y = 430, height = 150, width = 30)

ventana.mainloop()
