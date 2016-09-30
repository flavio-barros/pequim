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
            if(not p.pertence_cluster):
                if(p.id_taxista != ponto.id_taxista):
                    if (not self.vericar_pertinencia(p, vizinhos)):
                        if(Distancia().euclidiana(ponto, p) <= eps):
                            vizinhos.append(p)
        return vizinhos
    
    def expandir_cluster(self, ponto, c, eps, min_points, indice_cluster):
        ponto.pertence_cluster = True
        c.append(ponto)
        ponto.cluster = indice_cluster
        for p in ponto.vizinhos:
            p.visitado = True
            self.visitados+=1;
            print "{0} de {1} visitados - {2}".format(self.visitados, self.visitas, (100*self.visitados)/self.visitas)
            vizinhosp = []
            vizinhosp = self.consultar_regiao(p, eps)
            
            if(len(vizinhosp) >= min_points):
                ponto.vizinhos = self.uniao(ponto.vizinhos, vizinhosp)
        
            if(not p.pertence_cluster):
                p.pertence_cluster = True
                c.append(p)
                p.cluster = indice_cluster
    
    def db_scan(self, data_set, eps, min_points):
        self.visitas = len(data_set)
        self.visitados = 0
        self.pontos = data_set  
        clusters = []  
        indice_cluster = 0;    
        for p in data_set:
            if(not p.visitado):
                p.visitado = True
                self.visitados+=1;
                print "{0} de {1} visitados - {2}".format(self.visitados, self.visitas, (100*self.visitados)/self.visitas)
                p.vizinhos = self.consultar_regiao(p, eps)
#                 print "vizinhos de {0} :".format(p.id);
#                 for v in p.vizinhos:
#                     print "{}".format(v.id);
                if(len(p.vizinhos) < min_points):
                    p.tipo = "NOISE"
#                     print "Oi sou o ponto {} sou um NOISE".format(p.id)
                else:
                    cluster = []
                    clusters.append(cluster)
                    self.expandir_cluster(p, cluster, eps, min_points, indice_cluster)
                    indice_cluster+=1
                    print len(cluster)
                           
        x = 0
        for c in clusters:
            print "Cluster {}".format(x)
            x+=1
            for p in c:
                print "ID do ponto: {}".format(p.id)
                