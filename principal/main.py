'''
Created on 22 de set de 2016

@author: flavio-barros || amanda-sousa
''' 

from bancoDeDados.Conexao import Conexao

def main():
    
    c = Conexao().criar_conexao()
    cursor = c.cursor()
    
    sql = "select count(distinct id_taxista) from taxistas"
    
    cursor.execute(sql)

    taxistas = cursor.fetchall()
    
    for t in taxistas:
        print t[0]
    
if __name__ == '__main__':
    main()