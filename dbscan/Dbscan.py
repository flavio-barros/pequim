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
        print "Quantidade de vizinhos DISTINTOS do ponto {0} e:  {1}".format(p.id, len(lista))        
        return len(lista)
                    
    def consultar_regiao(self, ponto, eps):
        vizinhos = []
        for p in self.pontos:
#             if(abs(ponto.longitudeX - p.longitudeX) > eps):
#                 continue
#             elif(abs(ponto.latitudeY - p.latitudeY) > eps):
#                 continue
#             el
            if(Distancia().euclidiana(ponto, p) <= eps):
                vizinhos.append(p)
        
        return vizinhos
    
    def expandir_cluster(self, ponto, vizinhos, cluster, eps, min_points):
        ponto.pertence_cluster = True
        ponto.cluster = cluster
        for p in vizinhos:
            if(not p.visitado):
                p.visitado = True
                self.v+=1
                print "{}".format(self.v)
                vizinhosp = []
#                 print "Consultar regiao inicio"
                vizinhosp = self.consultar_regiao(p, eps)
#                 print "Consultar regiao fim"
                if(self.verificar_distintos(vizinhosp) >= min_points):
                    vizinhos = list(set(vizinhos).union(vizinhosp))
                            
            if(not p.pertence_cluster):
                p.pertence_cluster = True
                p.cluster = cluster
    
    def db_scan(self, data_set, eps, min_points):
        self.pontos = data_set  
        self.v = 0 
        cluster = 0;    
        for p in data_set:
            if(not p.visitado):
                p.visitado = True
                self.v+=1
                print "{}".format(self.v)
                vizinhos = self.consultar_regiao(p, eps)
                if(self.verificar_distintos(vizinhos) < min_points):
                    print "Ponto NOISE" 
                    p.tipo = "NOISE"
                else:
                    self.expandir_cluster(p, vizinhos, cluster, eps, min_points)
                    print "criando cluster{}".format(cluster)
                    cluster+=1