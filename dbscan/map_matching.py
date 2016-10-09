'''
Created on 8 de out de 2016

@author: amanda
'''
from math import sqrt
from dbscan.Dbscan import Distancia
from modelo.Ponto import Ponto

class MapMatching(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
        
        
    def distancia_perpendicular(self, ponto, x1, y1, x2, y2):
        
        cima = ((ponto.longitudeX * (y1-y2)) - (ponto.latitudeY * (x1-x2)) + (x1*y2 - x2*y1))
        ponto1 = Ponto(0,0,x1,y1)
        ponto2 = Ponto(0,0,x2,y2)
        baixo = Distancia().euclidiana (ponto1, ponto2)
        if(baixo == 0):
            return Distancia().euclidiana (ponto, ponto1)
        else:
            distancia = float(cima)/baixo 
            return abs(distancia)
    
    def matching(self, ponto, arestas):
        menor_distancia = self.distancia_perpendicular(ponto, arestas[0].origem_x, arestas[0].origem_y, arestas[0].destino_x, arestas[0].destino_y)
        aresta = arestas[0]
    
        for a in arestas:
            
            if(self.distancia_perpendicular(ponto, a.origem_x, a.origem_y, a.destino_x, a.destino_y) < menor_distancia):
                menor_distancia = self.distancia_perpendicular(ponto, a.origem_x, a.origem_y, a.destino_x, a.destino_y)
                aresta = a 
                
        return aresta
    
    def map_matching(self, pontos, arestas):
        count = 0
        for p in pontos:
            aresta = self.matching(p, arestas)
            p.longitudeX = aresta.origem_x
            p.latitudeY = aresta.origem_y
            print"{}".format(count)
            count+=1   