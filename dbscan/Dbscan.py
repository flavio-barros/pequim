'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''
from bancoDeDados.Conexao import Conexao
from dbscan.Distancia import Distancia
from mx.Tools.mxTools.mxTools import sizeof

class Dbscan(object):

    def __init__(self):
        self.pontos = Conexao.recuperar_pontos()
    
    def consultar_regiao(self, ponto, eps):
        vizinhos = []
        vizinhos.append(ponto)
        for p in self.pontos:
#             if(p.id_taxista != ponto.id_taxista):
            if(Distancia.euclidiana(self, ponto, p) <= eps):
                vizinhos.append(p)
        return vizinhos
    
    def expandir_cluster(self, ponto, vizinhos, c, eps, MinPts):
        ponto.pertence_cluster = True
        c.append(ponto)
        for p in vizinhos:
            p.visitado = True
            vizinhosp = []
            vizinhosp = self.consultar_regiao(p, eps)
            
            if(sizeof(vizinhosp) >= MinPts):
                vizinhos = list(set(vizinhos+vizinhosp))
        
            if(not p.pertence_cluster):
                p.pertence_cluster = True
                c.append(p)