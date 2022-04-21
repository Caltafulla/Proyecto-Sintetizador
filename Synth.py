#%%
import sounddevice as sd
import numpy as np
import tkinter


class nota:

    def _init_(self, n, o):
        self.n = n
        self.o = o


# Posiblemente se tenga en cuenta.
# class Octava():
    # def _init_ (self, o, n):
        # self.nota = []
        # for i in range(0, 12):
            # self.nota.append(nota(i, o))
        # pass

class piano:

    def _init_(self, n, o):
        self.o = nota(n, o)

    def frecuencia(self):
        expo = (int(self.o.o) - 4) * 12 + int(self.o.n) - 10
        return 440 * (2 * (1 / 12)) * expo


class VCO:

    def _init_(
        self,
        valoro,
        timbre,
        hz,
        volumenRL,
        name,
        onda=None,
        ):
        self.vo = valoro
        self.timbre = timbre
        self.hz = hz
        self.rl = volumenRL
        self.onda = Onda(name)


class VCO1(VCO):

    def _init_(
        self,
        valoro,
        timbre,
        hz,
        volumenRL,
        onda=None,
        ):
        super()._init_(valoro, timbre, hz, volumenRL, onda)


class VCO2(VCO):

    def _init_(
        self,
        valoro,
        timbre,
        hz,
        volumenRL,
        onda=None,
        ):
        super()._init_(valoro, timbre, hz, volumenRL, onda)


class VCO3(VCO):

    def _init_(
        self,
        valoro,
        timbre,
        hz,
        volumenRL,
        onda=None,
        ):
        super()._init_(valoro, timbre, hz, volumenRL, onda)


class Sonido:

    def _init_(self, volume, adsr):
        self.vol = volume
        self.adsr = adsr

    def GenerarSonido(wave):
        sd.play(wave, 44100)
        sd.wait()


class Filtro:

    def _init_(self, hz, tipo):
        self.hz = hz
        self.tipo = tipo


class ASDR:

    def _init_(
        self,
        a,
        s,
        d,
        r,
        ):
        self.a = a
        self.s = s
        self.d = d
        self.r = r


class Onda:

    def _init_(self, nombre):
        self.nombre = nombre

    def formula_onda():
        pass


class Sine:

    def _init_(self):
        pass

    def generar(hz):
        framerate = 44100
        time = 400
        t = np.linspace(0, time / 1000, int(framerate * time / 1000))
        wave = np.sin(2 * np.pi * hz * t)
        return wave


class Square(Onda):

    def _init_(self, nombre):
        pass


class Triangle(Onda):

    def _init_(self, nombre):
        pass


class Tipo_Onda:

    def _init_(self, TiopoOnda):
        self.to = TiopoOnda

# %%

ventana = tkinter.Tk()
ventana.geometry('380x130')
C = tkinter.Button(
    ventana,
    text='C',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(1,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
C.grid(row=0, column=0)
Cs = tkinter.Button(
    ventana,
    text='C#',
    fg='white',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(2,
            3).frecuencia())),
    width=2,
    height=4,
    bg='black',
    )
Cs.grid(row=0, column=1)
D = tkinter.Button(
    ventana,
    text='D',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(3,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
D.grid(row=0, column=2)
Ds = tkinter.Button(
    ventana,
    text='D#',
    fg='white',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(4,
            3).frecuencia())),
    width=2,
    height=4,
    bg='black',
    )
Ds.grid(row=0, column=3)
E = tkinter.Button(
    ventana,
    text='E',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(5,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
E.grid(row=0, column=4)
F = tkinter.Button(
    ventana,
    text='F',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(6,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
F.grid(row=0, column=5)
Fs = tkinter.Button(
    ventana,
    text='F#',
    fg='white',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(7,
            3).frecuencia())),
    width=2,
    height=4,
    bg='black',
    )
Fs.grid(row=0, column=6)
G = tkinter.Button(
    ventana,
    text='G',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(8,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
G.grid(row=0, column=7)
Gs = tkinter.Button(
    ventana,
    text='G#',
    fg='white',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(9,
            3).frecuencia())),
    width=2,
    height=4,
    bg='black',
    )
Gs.grid(row=0, column=8)
A = tkinter.Button(
    ventana,
    text='A',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(10,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
A.grid(row=0, column=9)
As = tkinter.Button(
    ventana,
    text='A#',
    fg='white',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(11,
            3).frecuencia())),
    width=2,
    height=4,
    bg='black',
    )
As.grid(row=0, column=10)
B = tkinter.Button(
    ventana,
    text='B',
    command=lambda : Sonido.GenerarSonido(Sine.generar(piano(12,
            3).frecuencia())),
    width=4,
    height=8,
    bg='white',
    )
B.grid(row=0, column=11)
ventana.mainloop()
 # %%
