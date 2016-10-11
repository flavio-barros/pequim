'''
Created on 9 de out de 2016

@author: amanda
'''
from modelo.Vertice import Vertice

class Aresta(object):
    
    def __init__(self, origem, destino, custo):
        self.origem = origem
        self.destino = destino
        self.custo = custo
    
    
    