from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []
    
    def __str__(self):
        x= f'Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte'
        return x


    def __init__(self, name, age, alt, sex, años, golesMarc, tarjetasRojas, habilFoot):
        Persona.__init__(self,name, age, alt, sex)
        Deportista.__init__(self,'Futbol',años)
        self._golesMarcados = golesMarc
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = habilFoot
        Futbolista._listaFutbolistas.append(self)


    #SET Y GET
    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    @classmethod
    def getListaFutolistas(cls):
        return cls._listaFutbolistas

    

    def setGolesMarcados(self, j):
        self._golesMarcados = j

    def setTarjetasRojas(self, j):
        self._tarjetasRojas = j

    def setPiernaHabil(self, j):
        self._piernaHabil = j


    
