# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:45:03 2022

@author: Kamilla Alves
"""

from contato import Contato


def menu():
    print('********** Agenda Telefônica **********')
    print('Menu')
    print('1 - Adicionar contato')
    print('2 - Adicionar varios contatos')
    print('3 - Pesquisar contato')
    print('4 - Remover contato')
    print('5 - Alterar contato')
    print('6 - Relatório ')
    print('7 - Salvar contatos')
    print('8 - Sair')
    opcao = input('Por gentileza, escolha uma opção: ')
    return opcao 
    

    
def digite_nome():
    return input('Digite o nome do contato:').lower()



def adicionar():
    print('Opção escolhida: Adicionar contato')
    contato = Contato(len(agenda) + 1)
    agenda[contato.nome.lower()] = contato
    print('')
    print('Adicionado com sucesso!')
 
    

def adicionar_varios():
    print('Opção escolhida: Adicionar varios contatos')
    quantidade = int(input('Digite a quantidade de contatos que deseja inserir: '))
    for item in range(quantidade):
        contato = Contato(len(agenda)+ 1)
        agenda[contato.nome.lower()] = contato
        print('')
        print('Adicionado com sucesso!')
    
    
    
def pesquisar():
    print('Opção escolhida: Pesquisar contato')
    contato = agenda.get(digite_nome())
    
    if contato == None:
        print('Contato inexistente')
    
    else: 
        print(contato)
        
    
def remover():
    print('Opção escolhida: Remover contato')
    contato = agenda.pop(digite_nome())
    print('O contato {0} deletado!'.format(contato.nome))
    
    
def alterar():
    print('Opção escolhida: Alterar contato')
    contato = agenda.get(digite_nome())
    if contato != None:
        contato.altera()
        agenda[contato.nome.lower()] = contato
        print('Alterado com sucesso!')
        

def relatorio(): 
    print('Opção escolhida: Relatório')
    formato = '''|{: >10}|{: >10}|{: >13}|{: >30}|{: >15}|{: >15}|\n'''
    
    cadastrados = formato.format('Numero:', 
                                 'Nome:', 
                                 'Telefone:', 
                                 'E-mail:', 
                                 'Twitter', 
                                 'Instagram:')
    
    
    for contato in agenda.values(): 
      cadastrados = cadastrados + formato.format(contato.id,
                                                 contato.nome, 
                                                 contato.telefone, 
                                                 contato.email, 
                                                 contato.twitter, 
                                                 contato.instagram)
      
    print(cadastrados)
      
def salvar():
    print('Opção escolhida: Salvar contatos')
    f = open('./contatos.txt', 'w')
    for contato in agenda.values():
        f.write(f'{contato.id},{contato.nome},{contato.telefone},{contato.email},{contato.twitter},{contato.instagram}\n')
    f.close()
    print('\nExportação feita com Sucesso!')
    

def inicializacao():
    
    for line in open('./contatos.txt', 'r'):
        contato = Contato() 
        contato.preenche(line)
        agenda[contato.nome.lower()] = contato


operacoes = {
    '1': adicionar,
    '2': adicionar_varios,
    '3': pesquisar,
    '4': remover, 
    '5': alterar,
    '6': relatorio,
    '7': salvar}


agenda = {}    
inicializacao() 
while True:
    opcao = menu()
    
    operacao = operacoes.get(opcao)
    
    if operacao != None:
        operacao()
    
    if opcao == '8': 
        break
    
    print('')
    print('')
    print('_______________________________________')
    


