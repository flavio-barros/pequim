'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
'''

import psycopg2
from modelo.Ponto import Ponto
from modelo.Aresta import Aresta
from gi.overrides.keysyms import cursor

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
        day = 3
        sql = "select id, id_taxista, longitude, latitude from taxistas where extract(day from hora) = {} limit 2000".format(day)
        
        cursor.execute(sql)
        
        pontosbd = cursor.fetchall()
        pontos = []
        
        self.encerrar_conexao(conexao)
        
        for p in pontosbd:
            ponto = Ponto(p[0], p[1], p[2], p[3])
            pontos.append(ponto)
            
        
        return pontos
    
    def recuperar_arestas(self):
        conexao = Conexao().criar_conexao()
        cursor = conexao.cursor()
        
        sql = "select v1.longitude, v1.latitude,v2.longitude, v2.latitude, e.distancia from estradas e, vertices v1, vertices v2 where e.origem = v1.id and e.destino = v2.id limit 2000";
        cursor.execute(sql)
       
        arestasbd = cursor.fetchall()
        arestas = []
   
        self.encerrar_conexao(conexao)
   
        for a in arestasbd:
            aresta = Aresta(a[0], a[1], a[2], a[3], a[4])
            arestas.append(aresta)
        return arestas
               
       
        
        
        