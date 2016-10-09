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
    
    
    def uniao(self, conjunto_a, conjunto_b):
        pertence = False
        for b in conjunto_b:
            for a in conjunto_a:
                if(b.id_taxista == a.id_taxista):
                    pertence = True
            if(not pertence):
                conjunto_a.append(b)
            pertence = False
        return conjunto_a
                
    def consultar_regiao(self, ponto, eps):
        vizinhos = []
        vizinhos.append(ponto)
        for p in self.pontos:
            if(Distancia().euclidiana(ponto, p) <= eps):
                if(not p.pertence_cluster):
                    if(p.id_taxista != ponto.id_taxista):
                        if (not self.vericar_pertinencia(p, vizinhos)):
                            vizinhos.append(p)
        return vizinhos
    
    def expandir_cluster(self, ponto, vizinhos, c, eps, min_points, indice_cluster):
        ponto.pertence_cluster = True
        c.append(ponto)
        ponto.cluster = indice_cluster
        for p in vizinhos:
            if(not p.visitado):
                p.visitado = True
                vizinhosp = []
                vizinhosp = self.consultar_regiao(p, eps)
            
                if(len(vizinhosp) >= min_points):
                    vizinhos = self.uniao(vizinhos, vizinhosp)
#                     vizinhos.extend(vizinhosp)
            if(not p.pertence_cluster):
                p.pertence_cluster = True
                c.append(p)
                p.cluster = indice_cluster
    
    def db_scan(self, data_set, eps, min_points):

        self.pontos = data_set  
        
        clusters = []  
        indice_cluster = 0;
        
        for p in data_set:
            if(not p.visitado):
                print "x"
                p.visitado = True
                vizinhos = self.consultar_regiao(p, eps)
                if(len(vizinhos) < min_points):
                    p.tipo = "NOISE"
                else:
                    cluster = []
                    clusters.append(cluster)
                    self.expandir_cluster(p, vizinhos, cluster, eps, min_points, indice_cluster)
                    indice_cluster+=1
                           
        x = 0
        for c in clusters:
            print "Cluster {}".format(x)
            x+=1
            for p in c:
                print "ID do ponto: {}".format(p.id)
                