"""
A FUNÇÃO reduce PERMITE REDUZIR UM CONJUNTO DE ELEMENTOS PARA UM ÚNICO VALOR, APLICANDO UMA
OUTRA FUNÇÃO NO PROCESSO.
NA ESTRUTURA DO reduce TEMOS:
x=reduce(<função>,<lista>)

PARA USAR ELA É NECESSÁRIO IMPORTAR
from functools import reduce

POR EXEMPLO, SOMAR TODOS OS VALORES DE UMA LISTA

#FUNÇÃO
def soma(a,b):
    return a+b

#PROGRAMA PRINCIPAL
lista= [1,2,3,4,5,6]
soma_total=reduce(soma,lista)
print(soma_total)

NESSE CÓDIGO, A CADA PAR DE VALOR DA LISTA É SOMADO E O RESULTADO É SOMADO AO VALOR SEGUINTE

1  2  3  4  5  6
 3    3  4  5  6
    6    4  5  6
      10    5  6
         15    6
            21

"""
from functools import reduce

def soma(a,b):
    return a+b

#PROGRAMA PRINCIPAL
lista= [1,2,3,4,5,6]
soma_total=reduce(soma,lista)
print(soma_total)