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
        c.commit()
        c.close()
        
            
    def recuperar_pontos(self):
        conexao = Conexao().criar_conexao()
        cursor = conexao.cursor()
        day = 02
        sql = "select id, id_taxista, longitude, latitude from taxistas where extract(day from hora) = {}".format(day)
        
        cursor.execute(sql)
        
        pontosbd = cursor.fetchall()
        pontos = []
        
        self.encerrar_conexao(conexao)
        
        for p in pontosbd:
            ponto = Ponto(p[0], p[1], p[2], p[3])
            pontos.append(ponto)
            
        
        return pontos