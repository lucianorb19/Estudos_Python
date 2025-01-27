"""
A FUNÇÃO zip UNE EM PARES ELEMENTOS DE DIFERENTES LISTAS. ELA PERMITE, NUM ÚNICO LAÇO, PERCORRER
MAIS DE UMA LISTA, DUAS, TRÊS....
SUA ESTRUTURA É
zip(<lista1>,<lista2>,<lista3>,...)

Exemplo
UNIR EM PARES OS ELEMENTOS DAS MESMAS POSIÇÕES DAS DUAS LISTA
x=[1,2,3,4]
y=["a","b","c","d",]

resultado = list(zip(x,y))
#resultado é [(1,'a'),(2,'b'),(3,'c'),(4,'d')]

SE NÃO CONSEGUIR COMBINAR, A FUNÇÃO DESCARTA
POR EXEMPLO, COMBINAR x='abcd' com y='12'
resultado: [('a','1'),('b','2')]
O c E d SÃO DESCARTADOS

PARA DICIONÁRIOS, POR PADRÃO, A FUNÇÃO ZIP COMBINA AS CHAVES
dic1={'a':'1','b':'2'}
dic2={'c':'3','d':'4'}
resultado=list(zip(dic1,dic2))
print(resultado)

SE QUISERMOS COMBINAR VALORES, SÓ USAR .values()

resultado=list(zip(dic1.values(),dic2.values()))
print(resultado)

TAMBÉM PODE SER FEITA UMA FUNÇÃO QUE USA A ZIP
POR EXEMPLO, UMA FUNÇÃO QUE USA A zip PARA SALVAR O RESULTADO DELA NUM DICIONÁRIO

#NESSA FUNÇÃO, É GERADO UM NOVO DICIONÁRIO A PARTIR DAS CHAVES DO PRIMEIRO E
#OS VALORES DO SEGUNDO
def criaDicionario(dic1,dic2):

    dicTemporario=dict()

    for dic1Chave,dic2Valor in zip(dic1,dic2.values())
        dicTemporario[dic1Chave]=dic2Valor

    return dicTemporario

# PROGRAMA PRINCIPAL
dicionario1 ={'a':'1','b':'2','c':'3',}
dicionario2 ={'d':'4','e':'5','f':'6',}
dicionario3=criaDicionario(dicionario1,dicionario2)
print(dicionario3)

"""


# NESSA FUNÇÃO, É GERADO UM NOVO DICIONÁRIO A PARTIR DAS CHAVES DO PRIMEIRO E
# OS VALORES DO SEGUNDO
def criaDicionario(dic1, dic2):
    dicTemporario = dict()

    for dic1Chave, dic2Valor in zip(dic1, dic2.values()):
        dicTemporario[dic1Chave] = dic2Valor

    return dicTemporario


# PROGRAMA PRINCIPAL
dicionario1 ={'a':'1','b':'2','c':'3',}
dicionario2 ={'d':'4','e':'5','f':'6',}
dicionario3=criaDicionario(dicionario1,dicionario2)
print(dicionario3)