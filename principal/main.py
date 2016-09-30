'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
''' 

from bancoDeDados.Conexao import Conexao
from dbscan.Dbscan import Dbscan
from modelo.Ponto import Ponto
from arquivosSaida.EscreverArquivo import EscreverArquivo

def main():
    
    #H = "select * from taxistas where extract(day from hora) = 02"
    data_set = Conexao().recuperar_pontos()
    eps = 10
    min_points = 4
    
    data_test = []
    data_test.append(Ponto(1, 1, 3, 4))
    data_test.append(Ponto(2, 2, 4, 4))
    data_test.append(Ponto(3, 3, 3, 4))
    data_test.append(Ponto(4, 4, 2, 4))
    data_test.append(Ponto(6, 5, 3, 9))
    data_test.append(Ponto(12, 6, 100, 102))
    data_test.append(Ponto(7, 7, 99, 96))
    data_test.append(Ponto(9, 8, 101, 103))
    data_test.append(Ponto(10, 9, 99, 98))
    data_test.append(Ponto(11, 10, 105, 106))
    data_test.append(Ponto(12, 11, 100, 97))
    data_test.append(Ponto(13, 12, 1, 2))
    data_test.append(Ponto(14, 13, 540, 4))
    data_test.append(Ponto(15, 14, 2, 3))
    

    db = Dbscan()

    db.db_scan(data_test, eps, min_points);
    
    EscreverArquivo().escrever(data_test)
    
if __name__ == '__main__':
    main()