'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''

class Ponto(object):

    def __init__(self, id, id_taxista, longitudeX, latitudeY):
        self.id = id
        self.id_taxista = id_taxista
        self.longitudeX = longitudeX
        self.latitudeY = latitudeY
        self.visitado = False
        self.pertence_cluster = False
        self.cluster = -1
        