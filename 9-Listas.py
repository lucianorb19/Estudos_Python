"""
LISTAS

#CRIAR LISTA
lista = []
lista = list()
lista = list(range(0,5)) - cria uma lista com os número de 0 a 4

#INSERIR NA LISTA
lista.append(x) - insere x no final da lista
lista.insert(a,x) - insere na posição a o elemento x

#REMOVER DA LISTA
lista.pop() - apaga o último elemento da lista
lista.remove(x) - apaga o elemento x da lista
del lista[x] - apaga o item da posição x
lista.pop(x) - apaga o item da posição x

#ENCONTRAR NA LISTA
lista.count(x) - conta quantas vezes o item de valor x aparece na lista

#ORDENAR LISTA
lista.sort()
lista.sort(reverse=True) ordena na ordem reversa
lista.reverse() - inverte a ordem da lista

#MOSTRAR LISTA
for x in lista:
    print("Eu vou comer {}!".format(x))

for cont in range(0,len(lista)):
    print("Eu vou comer {}, na posição {}".format(lista[cont], cont))

for pos,item in enumerate(lista):
    print("Eu vou comer {} na posição {}".format(item,pos))

#LIGAR DUAS LISTAS
a=[1,2,3]
b=a OQ ACONTECER EM b ACONTE EM a

COPIAR LISTA
a=[1,2,3]
b=a[:] #b recebe uma cópia dos elementos de a

#PARA QUALQUER ESTRUTURA DE REPETIÇÃO, O COMANDO continue PULA UMA ITERAÇÃO DO LAÇO
#POR EXEMPLO, MOSTRAR TODOS OS NOMES DA LISTA, MAS PULAR CASO O NOME SEJA LUCIANO

"""

from Pacote1 import verifica


#------------------------------------
print("DESAFIO - PULAR UM NOME NA LISTA")
nomes = ["GUSTAVO","AMANDA","LUCIANO","CLEBER",]

for nome in nomes:
    if nome=="LUCIANO":
        continue
    print(nome)
print()


#------------------------------------
print("DESAFIO - 5 VALORES NA LISTA")
#INICIALIZAÇÃO DAS VARIÁVEIS
numeros=[]
menor=1000
maior=0
pos_maior=pos_menor=0
lista_pos_maiores=[]
lista_pos_menores=[]

#LAÇO PARA INSERÇÃO DOS DADOS
for cont in range(0,5):
    valor=verifica.verifica_int(input(f"Digite o {cont+1}º valor: "))
    numeros.append(valor)#VALOR ADICIONADO À LISTA
    #VERIFICAÇÃO DO MAIOR E MENOR
    if valor>maior:
        maior=valor
    if valor<menor:
        menor=valor

#VERIFICAÇÃO DO VALOR MAIOR E MENOR, E EM QUAIS POSIÇÕES DA LISTA APARECEM
for pos,valor in enumerate(numeros):
    if valor==maior:
        lista_pos_maiores.append(pos)
    if valor==menor:
        lista_pos_menores.append(pos)


#MOSTRANDO OS RESULTADOS
print("Lista digitada: ",end="")
for valor in numeros:
    print(valor,end=" - ")
print()

#MENOR VALOR E SUAS POSIÇÕES
print(f"Menor valor: {menor},nas posições",end=" ")
for valor in lista_pos_menores:
    print(valor,end=" - ")
print()
#MAIOR VALOR E SUAS POSIÇÕES
print(f"Maior valor: {maior},nas posições",end=" ")
for valor in lista_pos_maiores:
    print(valor,end=" - ")
print()
print()


#------------------------------------
print("DESAFIO - VALORES ÚNICOS")
#INICIALIZAÇÃO DAS VARIÁVEIS
continuar=True
valores=[]


#ENQUANTO O USUÁRIO OPTAR POR CONTINUAR
while continuar:
    valor=verifica.verifica_int(input("Digite um número para a lista: "))
    if valor not in valores:#CASO O VALOR JÁ NÃO ESTEJA NA LISTA
        valores.append(valor)
    else:
        print("Valor desconsiderado. Já está na lista! ")

    #OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar [S/N] ? ")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar [S/N] ?")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False

#MOSTRANDO VALORES ÚNICOS DIGITADOS EM ORDEM CRESCENTE
valores.sort()
for valor in valores:
    print(valor,end=" - ")

#from operator import index
#maior que o maior - append
#menor que o menor - insert(0,x)
print()
print()


#------------------------------------
print("DESAFIO - INSERIR JÁ NA ORDEM")
numeros=[] #lista dos número ordenados
maior=0
menor=1000

for count in range(0,5):
    numero=verifica.verifica_int(input(f"Digite o {count+1}º valor: "))
    #DEFINIÇÃO DO VALOR MAIOR E DO MENOR
    if numero<=menor:
        menor=numero
    elif numero>=maior:
        maior=numero

    if len(numeros)==0:#se a lista estiver vazia, só insiro
        numeros.append(numero)

    elif len(numeros)==1:#se a lista tiver somente um número
        if numero>=numeros[0]:#e o número q eu for inserir agora for maior ou igual a ele
            numeros.append(numero)#insiro o número no final
        else:#caso o número seja menor
            numeros.insert(0,numero)#insiro ele na primeira posiçao

    elif len(numeros)==2:#caso a lista tenha tamanho 2
        if numeros[0]==numeros[1]:#se os dois da lista forem iguais
            if numero>=numeros[0]:#se o número a ser inserido for maior ou igual aos atuais
                numeros.append(numero)#insiro ele no final
            elif numero<numeros[0]:#se o número a ser inserido for menor que os atuais
                numeros.insert(0,numero)
        else:#caso os dois número da lista sejam diferentes
            #eles já estão inseridos ordenados, então o primeiro é menor que o segundo
            if numero<numeros[0]:#se ele for menor que o menor
                numeros.insert(0,numero)#insiro ele na primeira posição
            elif numero>=numeros[0] and numero<=numeros[1]:#se ele estiver entre os dois
                numeros.insert(1,numero)#insiro no meio deles
            elif numero>numeros[1]:#se ele for maior que o maior
                numeros.append(numero)#insiro no final

    else:#caso já tenha 3 números ou mais
        for atual in range(1,(len(numeros)-1)):#laço q vai do segundo ao penúltimo elemento
            numero_atual=numeros[atual]
            numero_proximo=numeros[atual+1] #atual, próximo e anterior
            numero_anterior=numeros[atual-1]
            #print(f"Atual {numero_atual}\nPróximo {numero_proximo}"
            #      f"\nAnterior {numero_anterior}")
            #print()

            #CASO O NÚMERO ESTEJA ENTRE OS AVALIADOS, FAÇO INSERÇÃO
            if numero>=numero_anterior and numero<=numero_proximo:
                #print("Entre os avaliados!")
                #X n X  X
                if numero == numero_anterior:
                    #print("Igual anterior")
                    numeros.insert(atual - 1, numero)
                    break
                #X n X  X
                elif numero <= numero_atual and numero >= numero_anterior:
                    #print("Menor ou igual atual e maior ou igual anterior")
                    numeros.insert(atual, numero)
                    break
                elif numero >= atual and numero <= numero_proximo:
                    #print("Maior ou igual atual e menor igual próximo")
                    numeros.insert(atual + 1, numero)
                    break

            #CASO NÃO ESTEJA ENTRE A LISTA, QUER DIZER QUE É O MAIOR OU O MENOR
            elif numero<=menor:#CASO SEJA O MENOR
                #print("Menor da lista")
                numeros.insert(0,numero)#INSIRO NO INÍCIO DA LISTA
                break
            elif numero>=maior:#CASO SEJA O MAIOR
                #print("Maior da lista")
                numeros.append(numero)#INSIRO NO FINAL DA LISTA
                break

    print("lista resultante: ",numeros)
print()


#------------------------------------
print("DESAFIO - VÁRIOS NÚMEROS NA LISTA")
'''
QUANTOS NÚMEROS FORAM INSERIDOS
LISTA ORDENADA DE MANEIRA DESCRESCENTE
SE O VALOR 5 ESTÁ NA LISTA
'''
continuar=True
numeros=[]
posicoes_5=[]

#ENQUANTO O USUÁRIO OPTAR POR CONTINUAR
while continuar:
    #ADICIONANDO NA LISTA E ORDENANDO
    numero=verifica.verifica_int(input("Digite um número inteiro para inserir na lista: "))
    numeros.append(numero)
    numeros.sort()

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False
print()

tamanho_lista=len(numeros)
numeros.sort(reverse=True)#SALVANDO A LISTA DESCRESCENTE
#print(numeros)
print(f"Quantos números foram inseridos na lista: {tamanho_lista}\n"
      f"Lista em ordem descrescente: {numeros}")


#CASO O 5 ESTEJA NA LISTA
if 5 in numeros:
    # LAÇO PARA SALVAR TODAS AS POSIÇÕES ONDE APARECE O VALOR 5
    for pos, numero in enumerate(numeros):
        if numero == 5:
            posicoes_5.append(pos)
    print("O valor 5 aparece na lista, nas posições...",end="")
    for x in posicoes_5:
        print(x,end=" - ")
else:
    print("O valor 5 não está na lista!")
print()
print()


#------------------------------------
print("DESAFIO - LISTAS DE PARES E ÍMPARES")
numeros=[]
pares=[]
impares=[]
continuar=True

while continuar:
    numero=verifica.verifica_int(input("Digite um número inteiro para a lista: "))
    numeros.append(numero)

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False

for numero in numeros:
    if numero%2==0:#SE NÚMERO FOR PAR
        pares.append(numero)
    else:#SE NÚMERO FOR ÍMPAR
        impares.append(numero)

print(f"Todos os números da lista: {numeros}\n"
      f"Números pares: {pares}\n"
      f"Números ímpares: {impares}\n")
print()


#------------------------------------
print("DESAFIO - EXPRESSÃO MATEMÁTICA CORRETA\n"
      "*parênteses fechados corretamente")
lista_expressao=[]
a=b=0

expressao=str(input("Digite uma expressão matemática:    *Use parênteses*\n"
                    "-> "))
#SALVANDO NA LISTA CADA CARACTERE - IGNORANDO ESPAÇOS
for caractere in expressao:
    if caractere!=" ":
        lista_expressao.append(caractere)

print(lista_expressao)

for caractere in lista_expressao:#CONTADOR DE CARACTERES ()
    if caractere=="(":
        a+=1
    if caractere==")":
        b+=1

#print(a,b)
if a!=b:
    print("Expressão inválida!")
else:
    print("Expressão válida!")
print()