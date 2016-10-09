'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
''' 

from bancoDeDados.Conexao import Conexao
from dbscan.Dbscan import Dbscan
from modelo.Ponto import Ponto
from arquivosSaida.EscreverArquivo import EscreverArquivo
from dbscan.map_matching import MapMatching

def main():
    
    print "Recuperando pontos"
    data_set = Conexao().recuperar_pontos()
    eps = 0.0005
    min_points = 25
    
    print "Recuperando arestas"
    arestas = Conexao().recuperar_arestas()
    
    MapMatching().map_matching(data_set, arestas)

      
    db = Dbscan()

    db.db_scan(data_set, eps, min_points)
    
    
    EscreverArquivo().escrever(data_set)
    
if __name__ == '__main__':
    main()