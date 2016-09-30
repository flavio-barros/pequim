'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''

from dbscan.Distancia import Distancia


class Dbscan(object):

    def __init__(self):
        pass
    
    
    def vericar_pertinencia(self, ponto, vizinhos):
        for p in vizinhos:
            if(ponto.id_taxista == p.id_taxista):
                return True
        return False
    
    def verificar_distintos(self, vizinhos):
        lista = []
        for p in vizinhos:
            if(not self.vericar_pertinencia(p, lista)):
                lista.append(p)
                
        return len(lista)
                    
    def consultar_regiao(self, ponto, eps):
        vizinhos = []
        vizinhos.append(ponto)
        for p in self.pontos:
            if(Distancia().euclidiana(ponto, p) <= eps):
                    vizinhos.append(p)
        return vizinhos
    
    def expandir_cluster(self, ponto, vizinhos, cluster, eps, min_points):
        ponto.pertence_cluster = True
        ponto.cluster = cluster
        
        for p in vizinhos:
            if(not p.visitado):
                p.visitado = True
                vizinhosp = []
                vizinhosp = self.consultar_regiao(p, eps)
            
                if(self.verificar_distintos(vizinhosp) >= min_points):
                    vizinhos.extend(vizinhosp)
        
            if(not p.pertence_cluster):
                p.pertence_cluster = True
                p.cluster = cluster
    
    def db_scan(self, data_set, eps, min_points):
        self.pontos = data_set    
        cluster = 0;    
        for p in data_set:
            if(not p.visitado):
                p.visitado = True
                vizinhos = self.consultar_regiao(p, eps)
                if(self.verificar_distintos(vizinhos) < min_points):
                    p.tipo = "NOISE"
                else:
                    self.expandir_cluster(p, vizinhos, cluster, eps, min_points)
                    cluster+=1