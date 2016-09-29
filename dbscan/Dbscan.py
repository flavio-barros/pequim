'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''
from bancoDeDados.Conexao import Conexao
from dbscan.Distancia import Distancia
from mx.Tools.mxTools.mxTools import sizeof

class Dbscan(object):

    def __init__(self):
        pass
    
    def consultar_regiao(self, ponto, eps):
        vizinhos = []
        vizinhos.append(ponto)
        for p in self.pontos:
            if(p.id_taxista != ponto.id_taxista):
                if(Distancia().euclidiana(ponto, p) <= eps):
                    vizinhos.append(p)
        return vizinhos
    
    def expandir_cluster(self, ponto, c, eps, min_points):
        ponto.pertence_cluster = True
        c.append(ponto)
        for p in ponto.vizinhos:
            p.visitado = True
            vizinhosp = []
            vizinhosp = self.consultar_regiao(p, eps)
            
            if(sizeof(vizinhosp) >= min_points):
                ponto.vizinhos = list(set(ponto.vizinhos+vizinhosp))
        
            if(not p.pertence_cluster):
                print "adicionando no cluster"
                p.pertence_cluster = True
                c.append(p)
    
    def db_scan(self, data_set, eps, min_points):
        self.pontos = data_set  
        clusters = []      
        for p in data_set:
            if(not p.visitado):
                p.visitado = True
                p.vizinhos = self.consultar_regiao(p, eps)
                if(len(p.vizinhos) < min_points):
                    p.tipo = "NOISE"
                    print "Oi sou o ponto {} sou um NOISE".format(p.id)
                else:
                    print "criando cluster"
                    cluster = []
                    clusters.append(cluster)
                    self.expandir_cluster(p, cluster, eps, min_points)
                    print len(cluster)
        
        x = 0
                
        for c in clusters:
            print "Cluster {}".format(x)
            x+=1
            for p in c:
                print "ID do ponto: {}".format(p.id)
                