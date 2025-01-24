"""
MANIPULAÇÃO DE STRINGS
frase='curso em video'
c u r s o   e m   v  i  d   e o
0 1 2 3 4 5 6 7 8 9 10 11  12 13

#FATIAMENTO
frase='Curso em Vídeo Python muito bom UAU'
#print(frase[a:b:c])
#a - início
#b - final (menos 1)
#c - passada

print(frase)
print(frase[6])#mostra o item na posição 6
print(frase[5:10])#mostra da posição 5 à 9 (um a menos no final)
print(frase[5:])#mostra a frase a partir da pos 5
print(frase[:5])#mostra a frase até a pos 4
print(frase[5:10:2])#mostra a frase da pos 5 a 9 pulando de dois em dois

#ANÁLISE
print(len(frase)) #número de caractéres da frase
print(frase.count('m')) #conta quantos 'm' tem na frase
print(frase.count('m',0,16)) #conta quantos 'm' tem na frase
                                            #da posição 0 à pos 15
print(frase.find('Pyt')) #se encontrar o trecho 'Pyt', mostra a posição inicial
                         #retorna -1 caso não encontre nada
print('Python' in frase) #Se existe o trecho 'Python' na frase, retorna True

#TRANSFORMAÇÃO
frase.replace('Python','Luciano') #gera uma frase substituindo 'Python' por 'Luciano'
frase.upper() #Torna a frase maiúscula
frase.lower() #torna a frase minúscula
frase.capitalize() #torna a primeira letra maiúscula, e as demais minúsculas
frase.title() #tornam maiúsculas todas letras iniciais das palavras
frase.strip()#retira os espaços vazios do começo e final da frase
frase.rstrip() #retira somente os espaços vazios do lado direito da frase (final)
frase.lstrip() #lado esquerdo

#DIVISÃO e JUNÇÃO
frase.split() #gera uma lista onde cada item é uma palavra da frase (separada por espaço)
'-'.join(frase) #gera uma string com a lista frase, separando cada item com '-'

#EXEMPLO
nome='laranja maça goiaba'
lista_dividida=nome.split()#gerando uma lista da frase, cada item da lista é um nome de fruta
print(lista_dividida[0]) #mostra o item da lista na posição 0 (laranja)
print(lista_dividida[0][2]) #mostra do item 0, a letra na pos 2 (r)
"""


#----------------------------------------------------------------------
print('DESAFIO - NOME E ALGUMAS INFORMAÇÕES DELE')
nome=input("Qual seu nome completo? ")
print("Nome todo maiúsculo: {}".format(nome.upper()))
print("Nome todo minúsculo: {}".format(nome.lower()))
lista_nome=nome.split() #gera uma lista com as palavras da frase
nomeNoespace=''.join(lista_nome) #gera uma frase sem espaços com cada item da lista
print("Número de letras da frase: {}".format(len(nomeNoespace)))
print("Número de letras de {}: {}".format(lista_nome[0],len(lista_nome[0])))#mostra o número de letras do primeiro nome
print()


#----------------------------------------------------------------------
print('DESAFIO - MOSTRAR OS DÍGITOS SEPARADOS DE UM NÚMERO')
numero=input(str("Digite um número de 4 dígitos: "))
print("Milhar:  {}\n"
      "Centena: {}\n"
      "Dezena: {}\n"
      "Unidade: {}\n".format(numero[0],numero[1],numero[2],numero[3]))
print()


#----------------------------------------------------------------------
print("DESAFIO - LER NOME DA CIDADE E VERIFICAR SE ELA COMEÇA COM 'SANTO' ")
cidade=input("Digite o nome da cidade: ")
cidade=cidade.upper() #deixando tudo maiúsculo
print("A cidade começa com 'SANTO': {}".format('SANTO' in cidade[0:5]))
print()


#----------------------------------------------------------------------
print("DESAFIO - VERIFICAR SE HÁ SILVA NO NOME DA PESSOA")
nome=input("Digite seu nome completo: ")
nome=nome.upper()#maiúsculo
print("{} tem 'SILVA' no nome: {}".format(nome,'SILVA' in nome))
print()


#----------------------------------------------------------------------
print("DESAFIO - UMA FRASE E ALGUMAS INFORMAÇÕES")
frase=input("Digite uma frase qualquer: ")
frase=frase.upper()#maiúsculo
print("Quantas vezes a letra 'A' aparece na frase: {}".format(frase.count('A')))
print("Em qual posição a letra 'A' aparece a primeira vez: {}".format(frase.find('A')))
print("Em qual posição a letra 'A' aparece pela última vez: {}".format(frase.rfind('A')))
print()


#----------------------------------------------------------------------
print("DESAFIO - MOSTRAR O PRIMEIRO E ÚTLIMO NOME DA PESSOA")
nome=input("Digite seu nome completo: ")
lista_nome1=nome.split()#fazendo uma lista com cada nome
print("Primeiro nome: {}".format(lista_nome1[0]))#primeiro item da lista
x=len(lista_nome1)
print("Último nome: {}".format(lista_nome1[x-1]))#último item da lista
print()