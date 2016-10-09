'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''
# from matplotlib.cbook import Null
import math
import sys
from modelo.No import No
class Distancia(object):



    def __init__(self):
        '''
        Constructor
        '''
    
    def euclidiana(self, ponto1, ponto2):
#         if(ponto1 != Null and ponto2 != Null):
        return math.hypot(ponto1.longitudeX - ponto2.longitudeX, ponto1.latitudeY - ponto2.latitudeY)
    
    def menor_caminho(self, ponto_origem, ponto_destino, arestas):
        if(ponto_origem.id_vertice == ponto_destino.id_vertice):
            return 0
        
        no = No(ponto_origem.id_vertice, 0)
        vizinhos = self.recuperar_vizinhos(no, arestas)
        vizinhos.sort( key=lambda v: v.custo)
        no = vizinhos.pop(0)
        while(no.id_vertice != ponto_destino.id_vertice):
            print "{}  --  {}".format(no.id_vertice, len(self.recuperar_vizinhos(no, arestas)))
            vizinhos.extend(self.recuperar_vizinhos(no, arestas))
            vizinhos.sort( key=lambda v: v.custo)
            if(len(vizinhos) == 0):
                return sys.maxint
            else:
                no = vizinhos.pop(0)
        return no.custo
    
    def recuperar_vizinhos(self, no, arestas):
        nos = []
        for a in arestas:
            if(no.id_vertice == a.origem.id_vertice):
                no = No(a.destino.id_vertice, no.custo+a.custo)
                nos.append(no)
        return nos