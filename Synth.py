#%%
import sounddevice as sd
import numpy as np

class nota():
    def __init__(self, n, o):
        self.n = n
        self.o = o
        
class Octava():
	def __init__ (self, o, n):
		# Se implementara mas adelante
		# self.nota = []
		# for i in range(0, 12):
			# self.nota.append(nota(i, o))
		pass
		
class piano():
	def __init__(self, n, o) -> None:
		self.o = nota(n, o)

	def frecuencia (self):
		expo = ((int(self.o.o) - 4) * 12) + ((int(self.o.n) - 10))
		return 440 * ((2**(1/12)) * expo)
	
class VCO():
	def __init__ (self, valoro, timbre, hz, volumenRL,name, onda = None):
		self.vo = valoro
		self.timbre = timbre
		self.hz = hz
		self.rl = volumenRL
		self.onda = Onda(name)

class VCO1 (VCO):
	def __init__ (self, valoro, timbre, hz, volumenRL, onda = None):
		super().__init__ (valoro, timbre, hz, volumenRL, onda)

class VCO2 (VCO):
    def __init__ (self, valoro, timbre, hz, volumenRL, onda = None):
        super().__init__(valoro,timbre,hz,volumenRL, onda)

class VCO3 (VCO):
	def __init__ (self, valoro, timbre, hz, volumenRL, onda = None):
		super().__init__ (valoro, timbre, hz, volumenRL, onda)

class Sonido():
	def __init__ (self, volume, adsr):
		self.vol = volume
		self.adsr = adsr
	def GenerarSonido (wave):
		sd.play(wave, 44100)
		sd.wait()

class Filtro ():	
	def __init__ (self, hz, tipo):
		self.hz = hz
		self.tipo = tipo

class ASDR():
	def __init__ (self, a, s, d, r):
		self.a = a
		self.s = s
		self.d = d
		self.r = r

class Onda ():
	def __init__ (self, nombre):
		self.nombre = nombre
	def formula_onda ():
		pass

class Sine():
	def __init__(self) -> None:
		pass
	def generar(hz):
		framerate = 44100
		time = 2500
		t = np.linspace(0, time/1000,int(framerate * time/1000))
		wave = np.sin(2*np.pi * hz * t)
		return wave

class Square (Onda):
	def __init__ (self,nombre):
		pass

class Triangle (Onda):
	def __init__ (self,nombre):
		pass

class Tipo_Onda ():
	def __init__ (self, TiopoOnda):
		self.to = TiopoOnda

n = input("Digite una nota: ")
o = input("Digite una octava: ")
p = piano(n, o)
hz1 = p.frecuencia()
wave = Sine.generar(hz1)
Sonido.GenerarSonido(wave)

# %%


