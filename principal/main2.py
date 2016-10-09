'''
Created on 8 de out de 2016

@author: amanda
'''
from modelo.Ponto import Ponto
from dbscan.Distancia import Distancia
import math

def main():
    
    p = Ponto(0,0,2.1,3.2)
    p2 = Ponto(0,0,4.2, 7.4)
    
    print math.hypot(2.1-4.2, 3.2-7.4)
    print Distancia().euclidiana(p, p2)

if __name__ == '__main__':
    main()