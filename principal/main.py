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
#     data_set = Conexao().recuperar_pontos()
    eps = 2
    min_points = 2
    
    data_test = []
    data_test.append(Ponto(1, 1, 1, 1))
    data_test.append(Ponto(2, 1, 1, 2))
    data_test.append(Ponto(3, 1, 1, 3))
    data_test.append(Ponto(4, 1, 2, 3))
    data_test.append(Ponto(5, 1, 3, 3))
    data_test.append(Ponto(6, 1, 4, 3))
    data_test.append(Ponto(7, 1, 5, 3))
    data_test.append(Ponto(8, 1, 5, 2))
    data_test.append(Ponto(9, 1, 5, 1))
    data_test.append(Ponto(10, 1, 6, 1))
    data_test.append(Ponto(11, 1, 7, 1))
    data_test.append(Ponto(12, 1, 7, 2))
    data_test.append(Ponto(13, 1, 7, 3))
    data_test.append(Ponto(14, 1, 7, 4))
    data_test.append(Ponto(15, 1, 7, 5))
    data_test.append(Ponto(16, 1, 7, 6))
    data_test.append(Ponto(17, 1, 6, 6))
    data_test.append(Ponto(18, 1, 5, 6))
    data_test.append(Ponto(19, 1, 4, 6))
    data_test.append(Ponto(20, 1, 3, 6))
    data_test.append(Ponto(21, 1, 2, 6))
    
    data_test.append(Ponto(22, 2, 2, 0))
    data_test.append(Ponto(23, 2, 2, 1))
    data_test.append(Ponto(24, 2, 2, 2))
    data_test.append(Ponto(25, 2, 2, 3))
    data_test.append(Ponto(26, 2, 2, 4))
    data_test.append(Ponto(27, 2, 3, 4))
    data_test.append(Ponto(28, 2, 4, 4))
    data_test.append(Ponto(29, 2, 5, 4))
    data_test.append(Ponto(30, 2, 6, 4))
    data_test.append(Ponto(31, 2, 6, 5))
    data_test.append(Ponto(32, 2, 6, 6))
    data_test.append(Ponto(33, 2, 5, 6))
    data_test.append(Ponto(34, 2, 4, 6))
    data_test.append(Ponto(35, 2, 3, 6))
    data_test.append(Ponto(36, 2, 2, 6))
    data_test.append(Ponto(37, 2, 1, 6))
    data_test.append(Ponto(38, 2, 1, 5))
    data_test.append(Ponto(39, 2, 0, 5))
    
    data_test.append(Ponto(40, 3, 3, 3))
    data_test.append(Ponto(41, 3, 3, 2))
    data_test.append(Ponto(42, 3, 3, 1))
    data_test.append(Ponto(43, 3, 3, 0))
    data_test.append(Ponto(44, 3, 4, 0))
    data_test.append(Ponto(45, 3, 4, 1))
    data_test.append(Ponto(46, 3, 4, 2))
    data_test.append(Ponto(47, 3, 4, 3))
    data_test.append(Ponto(48, 3, 4, 4))
    data_test.append(Ponto(49, 3, 4, 5))
    data_test.append(Ponto(50, 3, 5, 5))
    data_test.append(Ponto(51, 3, 6, 5))
    data_test.append(Ponto(52, 3, 7, 5))
      

    db = Dbscan()

    db.db_scan(data_test, eps, min_points);
    
    EscreverArquivo().escrever(data_test)
    
if __name__ == '__main__':
    main()