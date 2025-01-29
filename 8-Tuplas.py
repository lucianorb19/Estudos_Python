"""
Tupla - () imutável
Lista - []
Dicionários - {}

#MANEIRAS DE ACESSAR UMA TUPLA COM LAÇO FOR
lanche=("laranja","banana","goiaba","pera","suco")

for x in lanche:
    print("Eu vou comer {}!".format(x))

for cont in range(0,len(lanche)):
    print("Eu vou comer {}, na posição {}".format(lanche[cont], cont))

for pos,item in enumerate(lanche):
    print("Eu vou comer {} na posição {}".format(item,pos))

#MOSTRAR A TUPLA ORDENADA
print(sorted(lanche))

#CONCATENAR TUPLAS
a=(1,2,3)
b=(4,5,6)
c=a+b
print(c) - (1,2,3,4,5,6)

#MOSTRAR QUANTAS VEZES UM ITEM APARECE NA TUPLA
print(a.count(2)) - 1 pq o item 2 aparece uma vez na tupla a

#MOSTRAR O ÍNDICE DO ITEM 3
print(a.index(3)) - 2 pq o item 3 aparece na posição 2

#MOSTRAR O ÍNDICE DO ITEM 3 A PARTIR DA POSIÇÃO X
print(a.index(3,x))

#APAGAR A TUPLA DA MEMÓRIA (TAMBÉM SERVE PARA QUALQUER VARIÁVEL)
del(a) - apaga todos os dados da tupla a
"""

from Pacote1 import verifica

#-----------------------------------------------
print("DESAFIO - MOSTRAR VALORES POR EXTENSO")
#LISTA POR EXTENSO DE 0 A 20
numeros=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez"
         ,"onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito",
         "dezenove","vinte")

escolha=verifica.verifica_int(input("Digite um valor entre 0 e 20: "))
#ENQUANTO O NÚMERO DIGITADO NÃO FOR UM VALOR ENTRE 0 E 20, REPETE
while escolha<0 or escolha >20:
    print("Entrada inválida, tente novamente!")
    escolha = verifica.verifica_int(input("Digite um valor entre 0 e 20: "))
#MOSTRA O NÚMERO ESCOLHIDO POR EXTENSO
print("Você digitou o número {}".format(numeros[escolha]))
print()


#-----------------------------------------------
print("DESAFIO- TIMES CAMPEONATO BRASILEIRO")
times=("Botafogo","Palmeiras","Fortaleza","Flamengo","São Paulo",
       "Internacional","Bahia","Cruzeiro","Atlético-MG","Vasco",
       "Grêmio","Criciúma","Bragantino","Juventude","Athletico-PR",
       "Fluminense","Vitória","Corinthians","Cuiabá","Atlético-GO")

print("Primeiros cinco colocados: ")
for cont in range(0,5):
    print("{}º - {}".format(cont+1,times[cont]))
print()

print("Últimos 4 colocados: ")
for cont in range(19,15,-1):
    #print(cont)
    print("{}º - {}".format(cont+1,times[cont]))
print()

print("Times em ordem alfabética: ")
times_ordenado=sorted(times)
for item in times_ordenado:
    print(item)
print()

#COLOCAÇÃO BRAGANTINO
#COLOCAÇÃO COMEÇA DO 0. PRA FICAR BONITO, SOMA +1
colocacao=(times.index("Bragantino"))+1
print("Colocação Bragantino: {}º".format(colocacao))
print()


#-----------------------------------------------
print("DESAFIO - INSERIR 5 NÚMERO ALEATÓRIO NA TUPLA")
import time
from random import randint #BIBLIOTECA PARA GERAR NÚMERO ALEATÓRIO
n_aleatorios=[]#INICIALIZAÇÃO DA LISTA
maior=-1
menor=101

#GERAÇÃO DE CINCO NÚMERO ALEATÓRIOS ADICIONADOS À LISTA
print("Gerando número aleatórios para inserir na tupla: ",end="")
for cont in range(0,5):
    x=randint(0,100)#NÚMERO ENTRE 0 E 100
    print(x,end=" - ")
    time.sleep(0.5)
    n_aleatorios.append(x)#NÚMERO ADICIONADOS AO FINAL DA LISTA
    #VERIFICAÇÃO DE QUAL O MAIOR E MENOR DA LISTA
    for cont1 in n_aleatorios:
        if cont1>maior:
            maior=cont1
        if cont1<menor:
            menor=cont1
print()

n_aleatorios=tuple(n_aleatorios)#TORNANDO A LISTA UMA TUPLA
print("Tupla gerada: ",end="")
for item in n_aleatorios:
    print(item,end=" ")
print()

print("Maior: {}\nMenor: {}".format(maior,menor))
print()


#-----------------------------------------------
print("DESAFIO - 4 VALORES DA TUPLA")
valores=[] #LISTA PARA OS VALORES, QUE DEPOIS VIRA TUPLA
pares=[]

for cont in range(1,5):
    x=verifica.verifica_int(input("Digite o {}ºvalor: ".format(cont)))
    valores.append(x)#VALOR ADICIONADO À LISTA
    #COPIANDO OS VALORES PARES PARA OUTRA LISTA
    if x%2==0:
        pares.append(x)

#TRANSFORMANDO AS LISTAS EM TUPLAS
valores=tuple(valores)
pares=tuple(pares)

#TRATAMENTO SE O 9 APARECE NA TUPLA
if 9 in valores:
    print("Quantas vezes apareceu o valor 9: {}".format(valores.count(9)))
else:
    print("O valor 9 não apareceu nenhuma vez!")

#TRATAMENTO SE O 3 APARECE NA TUPLA
if 3 in valores:
    pos_3=valores.index(3)
    print("Em qual posição foi digitado o primeiro 3: {}ª".format(pos_3 + 1))
else:
    print("O valor 3 não foi digitado! ")

#MOSTRANDO VALORES PARES DA TUPLA
print("Valores pares da tupla: ",end="")
for item in pares:
    print(item,end=" - ")
print()
print()


#-----------------------------------------------
print("DESAFIO - LISTAGEM DE PREÇOS")
produtos=("Pão",3.5,"Manteiga",18.10,"Leite",4.80,"Frango",22.5,"Arroz",7.30)

#CABEÇALHO
print("-"*30)
print("LISTAGEM DE PREÇOS")
print("-"*30)

for cont in range(0,len(produtos),2):
    produto=produtos[cont]
    valor=produtos[cont+1]
    print("{}.....{}".format(produto,valor))
    #print(produto, valor)
print()


#-----------------------------------------------
print("DESAFIO - MOSTRAR VOGAIS DE CADA PALAVRA NA TUPLA")
frase=("GOIABA","LUCIANO","ANA","DOIS","CARLOS",)

for palavra in frase:
    print("Vogais de {}: ".format(palavra),end="")
    for letra in palavra:
        if letra in ["A","E","I","O","U"]:
            print(letra,end=" ")
    print()
print()