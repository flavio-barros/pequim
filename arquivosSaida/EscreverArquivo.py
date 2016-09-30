'''
Created on 30 de set de 2016

@author: flavio-barros
'''

import csv
from modelo.Ponto import Ponto

class EscreverArquivo(object):

    def __init__(self):
        self.id_estudante = "357420"
    
    def escrever(self, lista_pontos):
        c = csv.writer(open("pontos_clusterizados.csv", "wb"))
#         ["student_id", "id_taxista", "weekday", "latituide", "longitude", "cluster", "iscore"]
        cabecalho = ["student_id", "id_taxista", "longitude", "latituide"]
        c.writerow(cabecalho)
        
        for p in lista_pontos:
            c.writerow(self.ponto_para_lista(p))
        
    def ponto_para_lista(self, ponto):
        return [self.id_estudante, ponto.id_taxista, ponto.longitudeX, ponto.latitudeY]