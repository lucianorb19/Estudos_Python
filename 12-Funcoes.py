"""
FUNÇÕES
def nome():
    print("Luciano")

#PALAVRA def PARA CRIAR UMA FUNÇÃO
#ENTRE A FUNÇÃO E AS DEMAIS, NO MÍNIMO, DUAS LINHAS

#PODEM SER EXPLICITADOS OS PARÂMETROS DAS FUNÇÕES
def soma(a,b):
    s=a+b
    print(s)

#NO CÓDIGO PRINCIPAL
soma(a=2, b=4)
ou
soma(b=4, a=2)

#EMPACOTAMENTO DE PARÂMETROS
#PASSAR QUANTOS PARÂMETROS FOREM NECESSÁRIOS E O PYTHON GERENCIA
#POR EXEMPLO, UMA FUNÇÃO QUE CONTA QUANTOS PARÂMETROS FORAM PASSADOS
#NA FUNÇÃO
def contador(*num):
    tamanho=len(num)
    print(f"Os valores são {num} e ao todo são {tamanho} números")

#NO CÓDIGO PRINCIPAL
contador(1, 3, 4)
contador(2, 6, 7, 8, 2)
contador(1, 3)

#TAMBÉM É POSSÍVEL PASSAR UMA LISTA COMO PARÂMETRO. NESSE CASO NÃO É EMPACOTAMENTO, SOMENTE UMA FUNÇÃO
ESPECÍFICA QUE TRABALHA COM A LISTA. POR EXEMPLO, UMA FUNÇÃO QUE DOBRA TODOS OS VALORES DA LISTA RECEBIDA
def dobra(lista):
    pos=0 #posição na lista
    while pos<len(lista):#enquanto não chegar ao final da lista
        lista[pos]*=2 #cada item recebe o dobro do seu valor atual
        pos+=1 #incremento da posição

#NO CÓDIGO PRINCIPAL
valores=[2, 4, 5, 6, 2, 1]
dobra(valores)

#TAMBÉM É POSSÍVEL DEFINIR DENTRO DE UMA FUNÇÃO O COMPORTAMENTO pass, UTILIZADO PARA CRIAR UMA FUNÇÃO QUE NÃO FAZ NADA POR SÍ SÓ, MAS QUE SERVE DE BASE PARA OUTRAS APLICAÇÕES

def somar():
    pass
    
    
"""
from Pacote1 import verifica

#CONSTRUÇÃO DAS FUNÇÕES
import time
from random import randint
def f_area(a,b):
    area=a*b
    print(f"Área do terreno: {area} m²")


def escreva(a):
    tamanho=len(a)+4 #variável para auxiliar no print
    print("X"*tamanho)
    print(f"  {a:^}") #mensagem centralizada, 2 espacinhos vazios no print pra ficar bonito
    print("X" *tamanho)

def contador(inicio,fim,passo):
    if inicio<fim:
        fim = fim + 1  # para incluir o fim na contagem
        if passo<0:#caso seja crescente e o usuário coloque um passo negativo sem querer
            print("Nessa situação,o passo é crescente!")
            passo=abs(passo)

    elif inicio>fim:
        fim = fim - 1  # para incluir o fim na contagem
        if passo>0:#caso seja decrescente e o usuário coloque um valor positivo do passo sem querer
            print("Nessa situação, o passo é decrescente!")
            passo=passo-(2*passo) #tornando passo negativo

    if passo==0:#SE O PASSO FOR IGUAL A ZERO
        print("Não existe contagem com passo 0!")
        if inicio<fim:
            passo=1
            print("Passo redefinido para 1")
        elif inicio>fim:
            passo=-1
            print("Passo redefinido para -1")

    for x in range(inicio, fim, passo):
        print(x, end=" ")
        time.sleep(0.5)
    print()
    print("FIM! ")


def maior(numeros):
    #mostrando valores na tela
    print(f"Números digitados: {numeros}")
    print(f"Ao todo foram digitados {len(numeros)} valores")
    maior_num=numeros[0] #maior recebe primeiro valor dentre os parâmetros
    for x in numeros:#percorrer os parâmetros redefinindo o maior
        if x>maior_num:
            maior_num=x
    print(f"O maior número digitado foi {maior_num}")
    print("X"*30)


def sorteia(lista):
    for x in range(0,5):#LAÇO DE 5 REPETIÇÕES
        a=randint(0,100)#GERAÇÃO DE UM NÚMERO ALEATÓRIO ENTRE 0 E 100
        lista.append(a)#ADIÇÃO DESSE VALOR À LISTA PASSADA COMO PARÂMETRO
    print("Valores sorteados: ",end="")
    for x in lista:
        print(x, end="-")
    print()

def soma_pares(lista):
    soma=0
    for x in lista:
        if x%2==0:
            soma+=x
    print(f"Somando os valores pares da lista {lista}, temos {soma}")
    print("X"*30)



#CÓDIGO PRINCIPAL
#-------------------------------------------------------
print("DESAFIO -ÁREA DO TERRENO")
a1=verifica.verifica_float(input("Qual a largura do terreno em metros? "))
b1=verifica.verifica_float(input("E o comprimento em metros? "))
f_area(a1, b1)
print()


#-------------------------------------------------------
print("DESAFIO - ESCREVER MENSAGEM NA TELA COM TRATAMENTOS DE STRING")
mensagem=str(input("Digite sua mensagem: "))
escreva(mensagem)
print()


#-------------------------------------------------------
print("DESAFIO - CONTADOR COM INÍCIO FIM E PASSO")
#1º caso
#contador(1,10,1)
#2º caso
#contador(10,0,-2)
#3º caso
print("Agora é sua vez! ")
a1=verifica.verifica_int(input("Início: "))
b1=verifica.verifica_int(input("Fim: "))
c1=verifica.verifica_int(input("Passo: "))
contador(a1, b1, c1)
print()


#-------------------------------------------------------
print("DESAFIO - MAIOR NÚMERO")
continuar=True
lista=[]#LISTA A SER PASSADA COMO PARÂMETRO PARA A FUNÇÃO
while continuar:
    num=verifica.verifica_float(input("Digite um número para ser avaliado: "))
    lista.append(num) #NÚMERO ADICIONADO À LISTA
    #OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op=input("Deseja digitar outro número? [S/N]")
    op=op.upper()
    while op not in ["S","N","SIM","NÃO","NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op=="N" or op=="NÃO" or op=="NAO":
        continuar=False

maior(lista)
print()


#-------------------------------------------------------
print("DESAFIO - SORTEIO E SOMAR OS PARES")
numeros=list() #lista para o programa
sorteia(numeros)
soma_pares(numeros)
print()