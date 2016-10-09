'''
Created on 30 de set de 2016

@author: amanda
'''

from dbscan.Distancia import Distancia

class Teste(object):

    def __init__(self):
        pass

    def regiao(self, p, eps):
        print "verificando regiao de {}".format(p.id)
        vizinhos = []
        vizinhos.append(p)
        for q in self.pontos:
            dis = Distancia().euclidiana(p, q)
            if(dis <= eps):
                vizinhos.append(q)
                    
        return vizinhos            
    
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
        
    def expandir(self, p, vizinhos, cluster, eps, min_points):
        p.cluster = cluster
        for pp in vizinhos: 
            print "verificando a expansao do ponto {}".format(pp.id) 
            if(not pp.visitado):
                pp.visitado = True
                self.c+=1
                print"{}".format(self.c)
                vp = self.regiao(pp, eps)
                if(self.verificar_distintos(vp) >= min_points):
                    vizinhos.extend(vp)
                
            if(not pp.pertence_cluster):
                pp.pertence_cluster = True
                pp.cluster = cluster
                
                    
    def dbscan (self, D, eps, min_points):
        self.pontos = D
        self.c = 0
        cluster = 0
        for p in self.pontos:
            if(not p.visitado):
                p.visitado = True
                self.c+=1
                print"{}".format(self.c)
                vizinhos = self.regiao(p, eps)
                if(len(vizinhos) < min_points):
                    p.tipo = "NOISE"
                else:
                    p.tipo = "CORE"
                    cluster +=1
                    self.expandir(p, vizinhos, cluster, eps, min_points)
        print "Cluster {} acabou".format(cluster)