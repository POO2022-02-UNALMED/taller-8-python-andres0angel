class Deportista():

    def __init__(self, deporte, años):
        self._deporte = deporte
        self._añosPracticando = años


    #SET Y GET
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, sport):
        self._deporte = sport

    def getAñosPracticando (self):
        return self._añosPracticando

    def setAñosPracticando(self, practicing):
        self._añosPracticando = practicing



