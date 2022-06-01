class nota:
    #Constructor de la clase nota con los atributos o (Octava) y n (Numero de nota)
    #Numeros de notas:
    # Do: 1
    # Do#: 2
    # Re: 3
    # Re#: 4
    # Mi: 5
    # Fa: 6
    # Fa#: 7
    # Sol: 8
    # Sol#: 9
    # La: 10
    # La#: 11
    # Si: 12
    def __init__(self, n, o):
        self.n = n
        self.o = o

class piano:
    #Vector que contendra a varios objetos tipo nota
    o = []
    #Constructo de la clase piano que contiene los atributos ob (Octava base), hzb (Frecuencia base)
    #Semitone (Semitonos desplazados)
    def __init__(self, ob = 0, hzb = 440, semitone = 0):
        #Ciclos para agregar 24 objetos tipo nota al vector "o"
        for o in range (4, 6):
            for n in range (1, 13):
                self.o.append(nota(n, o))
        self.ob = ob
        self.hzb = hzb
        self.semitone = semitone

    #Metodo para obtener frecuencias de una nota dependiendo la frecuencia base y parametros
    # Parametros:
    # Semitone= Adicionales semitonos que se rodara la frecuencia
    # x= Posicion del vector "o" que se va a acceder (Esto depende a la nota que se quiera tocar)
    def frecuencia(self, semitone, x):
        expo = (int(self.o[x].o) - 4 + self.ob) * 12 + int(self.o[x].n) - 10 + semitone
        return self.hzb * (2 ** (1 / 12)) ** expo

    #Metodo para obtener frecuencias de una nota dependiendo la frecuencia de 440 y parametros
    # Parametros:
    # Semitone= Adicionales semitonos que se rodara la frecuencia
    # x= Posicion del vector "o", en este caso seria el de el La de la 4ta octava
    def frecuenciab(self, semitone, x = 4):
        expo = (int(self.o[x].o) - 4 + self.ob) * 12 + int(self.o[x].n) - 10 + semitone
        return 440 * (2 ** (1 / 12)) ** expo

    #Metodo para aumentar el atributo ob (Octava base) dependiendo del parametro "i" y si no
    #A tenido problemas con su confirmacion para saber si esta en el rango de -1 a 1
    def octavab (self, i):
        if (self.ob + i <= 1 and self.ob + i >= -1):
            self.ob = self.ob + i

    #Metodo para aumentar el atributo hzb (Frecuencia base) dependiendo del parametro "i" y si no
    #A tenido problemas con su confirmacion para saber si esta en el rango de -12 a 12
    def hzbase(self, i):
        if (self.semitone + i <= 12 and self.semitone + i >= -12):
            self.semitone = self.semitone + i
            self.hzb = self.frecuenciab(self.semitone, 9)