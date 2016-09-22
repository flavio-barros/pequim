'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''
from math import sqrt
class Distancia(object):



    def __init__(self, params):
        '''
        Constructor
        '''
    
    def euclidiana(self, ponto1, ponto2):
        return sqrt(pow((ponto1.longitudeX - ponto2.longitudeX), 2)
                        + pow((ponto1.latitudeY - ponto2.latitudeY), 2)) 