'''
Created on Tue Jul 17 09:42:06 2018
@author: Bruno Cruz, Francisco Ribeiro, Matheus Holanda, João Vínicius Rogrigues
'''
import random
from random import randint
from time import sleep
print('\nBem-Vindos, ao MASTERMIND') 
print('___' * 15)
print('')
print('        [ 1 ] - Nível \n            ')
print(' * A senha possui 4 digitos \n * Você tem exatamente 8 jogadas \n * A senha possui números distintos \n * A senha tem números de 0 a 4\n')
print('        [ 2 ] - Nível \n           ')
print(' * A senha possui 5 digitos \n * Você tem exatamente 10 jogadas \n * A senha possui números distintos \n * A senha tem números de 0 a 5\n')
print('        [ 3 ] - Nível \n            ')
print(' * A senha possui 6 digitos \n * Você tem exatamente 12 jogadas \n * A senha possui números distintos \n * A senha tem números de 0 a 6')
print('___' * 15)
continuar = 'S'
vt = 0
dt = 0
while continuar == 'S' :  
    nivel = int(input('Qual o nível você deseja? '))
    while nivel != 1 and nivel != 2 and nivel != 3:
        nivel = int(input('Nível invalido ! \nQual o nível você deseja? '))   
    if nivel == 1:
        quantidade_digitos = 4
        limite = 8 
        restantes = 8
        digitos = ('0','1','2','3','4')
        senha = ''
        for i in range(quantidade_digitos):
            escolhido = random.choice(digitos)
            while escolhido in senha:
                escolhido = random.choice(digitos)
            senha = senha + escolhido    
    elif nivel == 2:
        quantidade_digitos = 5
        limite = 10
        restantes = 10
        digitos = ('0','1','2','3','4','5')
        senha = ''
        for i in range(quantidade_digitos):
            escolhido = random.choice(digitos)
            while escolhido in senha:
                escolhido = random.choice(digitos)
            senha = senha + escolhido  
    elif nivel == 3:
        quantidade_digitos = 6
        limite = 12
        restantes = 12
        senha = ''
        senha = str(randint(0, 6))+ ""+str(randint(0, 6))+ ""+ str(randint(0, 6))+ ""+ str(randint(0, 6))+ ""+str(randint(0, 6))+ ""+str(randint(0, 6))        
    tentativas = 1 
    print('A SENHA ATUAL É : {}\n'.format(senha))
    print('Tente adivinhar uma senha de {} digitos distintos'.format(quantidade_digitos))
    proposta = str(input('A senha é? '))
    print('Procesando...')
    sleep(0.5)  
    while len(senha) != len(proposta):
            proposta = str(input('Senha invalida ! A senha tem exatamente {} digitos \nDigite a senha novamente? '.format(quantidade_digitos)))   
    sleep(0.5)
    while proposta != senha:
             tentativas = tentativas + 1
             acertos = 0
             conhecidencias = 0
             restantes = restantes - 1
             for i in range(quantidade_digitos):
                 if proposta[i] == senha[i]:
                     acertos = acertos + 1
                 elif proposta[i] in senha:
                     conhecidencias = conhecidencias + 1
             print('Sua proposta foi {} tem {} ACERTO(s) e {} CONHECIDENCIA(s)'.format(proposta,acertos,conhecidencias))
             print('Restam {} tentativa(s)'.format(restantes))
             if tentativas <= limite:
                 proposta = str(input('Tente novamente... A senha é? '))
                 print('Procesando...')
                 sleep(0.5)
                 while len(senha) != len(proposta):
                     proposta = str(input('A senha é? '))
             if tentativas > limite:
                     print('\nVocê Perdeu! Já foram {} TENTATIVAS(s)'.format(tentativas-1))
                     print('A senha era: {}'.format(senha))
                     dt = dt + 1
                     break    
    if nivel == 1 and tentativas <= 8:
        print('\nBoa! quero ver conseguir com menos tentativa(s). \nNo total foram {} tentativa(s)'.format(tentativas))
        print('A senha era: ',senha)
        vt = vt + 1
        continuar = str(input('Deseja jogar novamente? [SIM ou NÃO] ')).upper().strip()[0]
    if nivel == 2 and tentativas <= 10:
        print('\nBoa! quero ver conseguir com menos tentativas. No total foram {} tentativa(s)'.format(tentativas))
        print('A senha era: ',senha) 
        vt = vt + 1
        continuar = str(input('Deseja jogar novamente? [SIM ou NÃO] ')).upper().strip()[0]
    if nivel == 3 and tentativas <= 12:
        print('\nBoa! quero ver conseguir com menos tentativas. No total foram {} tentativa(s)'.format(tentativas))
        print('A senha era: ',senha)
        vt = vt + 1
        continuar = str(input('Deseja jogar novamente? [SIM ou NÃO] ')).upper().strip()[0]
    elif tentativas > limite:
        continuar = str(input('Deseja jogar novamente? [SIM ou NÃO] ')).upper().strip()[0]
print('\nFIM DE JOGO')    
print('''\nPLACAR FINAL\n
TOTAL DERROTA(s) = {}
TOTAL VITÓRIA(s) = {} '''.format(dt, vt))




























