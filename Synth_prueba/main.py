#%%

import tkinter
import matplotlib.pyplot as plt
from onda import Saw, Sine, Square
from ganancia import play
from genp import piano

o = input("¿En que octava deseas trabajar?: ")
tipo = input("1. Sine, 2. Square, 3. Triangle, 4. Sierra")
ventana = tkinter.Tk()
ventana.geometry('380x130')
if (int(tipo) == 1):
    C = tkinter.Button(
        ventana,
        text='C',
        command=lambda : play.GenerarSonido(Sine.generar(piano(1,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    C.grid(row=0, column=0)
    Cs = tkinter.Button(
        ventana,
        text='Cs',
        fg='white',
        command=lambda : play.GenerarSonido(Sine.generar(piano(2,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Cs.grid(row=0, column=1)
    D = tkinter.Button(
        ventana,
        text='D',
        command=lambda : play.GenerarSonido(Sine.generar(piano(3,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    D.grid(row=0, column=2)
    Ds = tkinter.Button(
        ventana,
        text='Ds',
        fg='white',
        command=lambda : play.GenerarSonido(Sine.generar(piano(4,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Ds.grid(row=0, column=3)
    E = tkinter.Button(
        ventana,
        text='E',
        command=lambda : play.GenerarSonido(Sine.generar(piano(5,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    E.grid(row=0, column=4)
    F = tkinter.Button(
        ventana,
        text='F',
        command=lambda : play.GenerarSonido(Sine.generar(piano(6,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    F.grid(row=0, column=5)
    Fs = tkinter.Button(
        ventana,
        text='Fs',
        fg='white',
        command=lambda : play.GenerarSonido(Sine.generar(piano(7,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Fs.grid(row=0, column=6)
    G = tkinter.Button(
        ventana,
        text='G',
        command=lambda : play.GenerarSonido(Sine.generar(piano(8,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    G.grid(row=0, column=7)
    Gs = tkinter.Button(
        ventana,
        text='Gs',
        fg='white',
        command=lambda : play.GenerarSonido(Sine.generar(piano(9,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Gs.grid(row=0, column=8)
    A = tkinter.Button(
        ventana,
        text='A',
        command=lambda : play.GenerarSonido(Sine.generar(piano(10,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    A.grid(row=0, column=9)
    As = tkinter.Button(
        ventana,
        text='As',
        fg='white',
        command=lambda : play.GenerarSonido(Sine.generar(piano(11,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    As.grid(row=0, column=10)
    B = tkinter.Button(
        ventana,
        text='B',
        command=lambda : play.GenerarSonido(Sine.generar(piano(12,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    B.grid(row=0, column=11)
elif (int(tipo) == 2):
    C = tkinter.Button(
        ventana,
        text='C',
        command=lambda : play.GenerarSonido(Square.generar(piano(1,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    C.grid(row=0, column=0)
    Cs = tkinter.Button(
        ventana,
        text='Cs',
        fg='white',
        command=lambda : play.GenerarSonido(Square.generar(piano(2,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Cs.grid(row=0, column=1)
    D = tkinter.Button(
        ventana,
        text='D',
        command=lambda : play.GenerarSonido(Square.generar(piano(3,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    D.grid(row=0, column=2)
    Ds = tkinter.Button(
        ventana,
        text='Ds',
        fg='white',
        command=lambda : play.GenerarSonido(Square.generar(piano(4,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Ds.grid(row=0, column=3)
    E = tkinter.Button(
        ventana,
        text='E',
        command=lambda : play.GenerarSonido(Square.generar(piano(5,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    E.grid(row=0, column=4)
    F = tkinter.Button(
        ventana,
        text='F',
        command=lambda : play.GenerarSonido(Square.generar(piano(6,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    F.grid(row=0, column=5)
    Fs = tkinter.Button(
        ventana,
        text='Fs',
        fg='white',
        command=lambda : play.GenerarSonido(Square.generar(piano(7,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Fs.grid(row=0, column=6)
    G = tkinter.Button(
        ventana,
        text='G',
        command=lambda : play.GenerarSonido(Square.generar(piano(8,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    G.grid(row=0, column=7)
    Gs = tkinter.Button(
        ventana,
        text='Gs',
        fg='white',
        command=lambda : play.GenerarSonido(Square.generar(piano(9,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Gs.grid(row=0, column=8)
    A = tkinter.Button(
        ventana,
        text='A',
        command=lambda : play.GenerarSonido(Square.generar(piano(10,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    A.grid(row=0, column=9)
    As = tkinter.Button(
        ventana,
        text='As',
        fg='white',
        command=lambda : play.GenerarSonido(Square.generar(piano(11,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    As.grid(row=0, column=10)
    B = tkinter.Button(
        ventana,
        text='B',
        command=lambda : play.GenerarSonido(Square.generar(piano(12,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    B.grid(row=0, column=11)
elif (int(tipo) == 3):
    C = tkinter.Button(
        ventana,
        text='C',
        command=lambda : play.GenerarSonido(Saw.generar(piano(1,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    C.grid(row=0, column=0)
    plt.plot(Saw.generar(piano(1, o).frecuencia())[:1000])
    plt.show()
    Cs = tkinter.Button(
        ventana,
        text='Cs',
        fg='white',
        command=lambda : play.GenerarSonido(Saw.generar(piano(2,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Cs.grid(row=0, column=1)
    D = tkinter.Button(
        ventana,
        text='D',
        command=lambda : play.GenerarSonido(Saw.generar(piano(3,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    D.grid(row=0, column=2)
    Ds = tkinter.Button(
        ventana,
        text='Ds',
        fg='white',
        command=lambda : play.GenerarSonido(Saw.generar(piano(4,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Ds.grid(row=0, column=3)
    E = tkinter.Button(
        ventana,
        text='E',
        command=lambda : play.GenerarSonido(Saw.generar(piano(5,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    E.grid(row=0, column=4)
    F = tkinter.Button(
        ventana,
        text='F',
        command=lambda : play.GenerarSonido(Saw.generar(piano(6,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    F.grid(row=0, column=5)
    Fs = tkinter.Button(
        ventana,
        text='Fs',
        fg='white',
        command=lambda : play.GenerarSonido(Saw.generar(piano(7,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Fs.grid(row=0, column=6)
    G = tkinter.Button(
        ventana,
        text='G',
        command=lambda : play.GenerarSonido(Saw.generar(piano(8,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    G.grid(row=0, column=7)
    Gs = tkinter.Button(
        ventana,
        text='Gs',
        fg='white',
        command=lambda : play.GenerarSonido(Saw.generar(piano(9,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    Gs.grid(row=0, column=8)
    A = tkinter.Button(
        ventana,
        text='A',
        command=lambda : play.GenerarSonido(Saw.generar(piano(10,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    A.grid(row=0, column=9)
    As = tkinter.Button(
        ventana,
        text='As',
        fg='white',
        command=lambda : play.GenerarSonido(Saw.generar(piano(11,
                o).frecuencia())),
        width=2,
        height=4,
        bg='black',
        )
    As.grid(row=0, column=10)
    B = tkinter.Button(
        ventana,
        text='B',
        command=lambda : play.GenerarSonido(Saw.generar(piano(12,
                o).frecuencia())),
        width=4,
        height=8,
        bg='white',
        )
    B.grid(row=0, column=11)
    
ventana.mainloop()

# %%
