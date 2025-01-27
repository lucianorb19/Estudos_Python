"""
List Comprehension É UMA MANEIRA DIFERENTE DE SE ESCREVER O PROCESSAMENTO SOBRE UMA LISTA
O CÓDIGO QUE ELEVA AO QUADRADO TODOS OS ELEMENTOS DE UMA LISTA PODE SER ESCRITO ASSIM

a=[2,4,6,8]
b=[]
for item in a:
    b.append(item**2)

print(a)
print(b)

OU PODEMOS USAR O list comprehension E ESCREVER ASSIM
FÓRMULA DO list comprehension
lista = [<operação><laço><condição>]
PRIMEIRO UM EXEMPLO SEM CONDIÇÃO, QUE FAZ O MESMO DO 1º EXEMPLO

a=[2,4,6,8]
b=[item**2 for item in a]

AGORA UM EXEMPLO USANDO CONDIÇÃO, QUE VAI SALVAR APENAS OS VALORES ÍMPARES DA LISTA, NA OUTRA
a=[1,2,3,4,5,6]
b=[item for item in a if item%2==1]

ESSA APLICAÇÃO DO list comprehension SALVA NA LISTA b APENAS OS NÚMEROS ÍMPARES DA LISTA A
"""

a=[1,2,3,4,5,6]
b=[item for item in a if item%2==1]

print(a)
print(b)