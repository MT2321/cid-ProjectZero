'''   Clase
- Recibe las matrices
- Recibe el vocabulario (dict)
- dict{word, sim} findSimilar(V, threshold, year)
- lista histSimilar(V, threshold)
- array getVector(word, year)
- getVector(positives = [], negatives = [], year)
- getSim(w1, y1, w2, y2)
- getEvol(w1, y1, w2)
- list(year-1) getEvolByStep(w1)
'''

class tempName:
    def __init__(self, matrixes, vocabulary):
        self.matrixes = matrixes
        self.vocabulary = vocabulary

    def findSimilar(self, vector, threshold, year):
        if type(threshold) is float:
            pass
            # se busca similitud coseno
        elif type(threshold) is int:
            pass
            # se busca por cantidad
        
        resultados = {} # diccionario con las palabras encontradas y su sim-cos respecto de la ingresada

        return resultados

    def histSimilar(self, vector, threshold):
        histograma = []

        return histograma

    def getVector(self, word, year):
        vector = []

        return vector

    def getVectorPosNeg(self, positives, negatives, year):
        vector = []

        return vector

    def getSim(self, w1, y1, w2, y2):
        return cosSim
    
    def getEvol(self, w1, y1, w2):
        return evol

    def getEvolByStep(self, word):
        evolution = []

        return evolution