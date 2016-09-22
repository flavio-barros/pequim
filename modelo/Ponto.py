'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''

class Ponto(object):

    def __init__(self, id, id_taxista, longitudeX, latitudeY, vizinhos, tipo):
        self.id = id
        self.id_taxista = id_taxista
        self.longitudeX = longitudeX
        self.latitudeY = latitudeY
        self.vizinhos = vizinhos
        self.tipo = tipo
        self.visitado = False
        self.pertence_cluster = False
        