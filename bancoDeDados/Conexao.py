'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''

import psycopg2
from modelo.Ponto import Ponto

class Conexao(object):

    def __init__(self):
        self.host='localhost'
        self.database='taxi-pequim'
        self.user='postgres'
        self.password = 'postgres'
    
    def criar_conexao(self):
        try:
            return psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        except Exception:
            print Exception
            
    def encerrar_conexao(self, c):
        c.close()
        c.commit()
            
    def recuperar_pontos(self):
        conexao = Conexao().criar_conexao()
        cursor = conexao.cursor()
        
        sql = "select id, id_taxista, longitude, latitude from taxistas"
        
        cursor.execute(sql)
        
        pontosbd = cursor.fetchall()
        pontos = []
        
        for p in pontosbd:
            ponto = Ponto()
            ponto.id = p[0]
            ponto.id_taxista = p[1]
            ponto.longitudeX = p [2]
            ponto.latitudeY = p[3]
            
            pontos.append(ponto)
            
        return pontos    