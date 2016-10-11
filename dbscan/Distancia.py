'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''
from matplotlib.cbook import Null
import math
class Distancia(object):


    def __init__(self):
        '''
        Constructor
        '''
    
    def euclidiana(self, ponto1, ponto2):
        if(ponto1 != Null and ponto2 != Null):
            return math.hypot(ponto1.longitudeX - ponto2.longitudeX, ponto1.latitudeY - ponto2.latitudeY)
        
        
    
    def menor_caminho(self):