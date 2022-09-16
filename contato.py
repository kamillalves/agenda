# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:46:34 2022

@author: Kamilla Alves
"""



class Contato:
    formato = '''|{: >10}|{: >10}|{: >20}|{: >15}|{: >15}|\n'''
    
    def __init__(self, id=None):
        
        if(id != None):
            self.id = id
            self.nome = input('Nome:')
            self.altera()
        

    def altera(self): 
         self.telefone = input('Telefone:')
         self.email = input('E-mail:')
         self.twitter = input('Twitter:')
         self.instagram = input('Instagram:')
         
         
    def __repr__(self):
        labels = self.formato.format('Nome', 'Telefone', 'E-mail', 'Twitter', 'Instagram')
        valores = self.formato.format(*[self.nome, self.telefone, self.email, self.twitter, self.instagram])
        return  labels + valores
    
    def preenche(self, linha):
        valores = linha.split(',') 
        self.id = valores[0] 
        self.nome = valores[1] 
        self.telefone = valores[2]
        self.email = valores[3]
        self.twitter = valores[4]
        self.instagram = valores[4]
        
        


       
