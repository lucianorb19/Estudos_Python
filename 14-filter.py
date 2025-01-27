"""
FILTRA UMA ESTRUTURA DE DADOS BASEADO EM UMA CONDIÇÃO
SE RESULTAR EM TRUE, RETORNA O VALOR, SE NÃO, IGNORA

EXEMPLO, SALVAR OS NÚMEROS PARES DE UMA LISTA EM OUTRA
def par(valor):
    if valor%2==0:
        return valor

a=[1,2,3,4,5,6]
b=list(filter(par,a))
print(b) #somente os pares

"""


def pares(valor):
    if valor % 2 == 0:
        return valor


a = [1, 2, 3, 4, 5, 6]
b = list(filter(pares, a))
print(b)  # somente os pares