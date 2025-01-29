"""
for x in range(inicio,fim,passo):
    codigo

for c in range(1,10) - 9 repetições - de 1 a 9
for c in range(0,10) - 10 repetições - de 0 a 9
for c in range(0,10,2) - Passo 2 ao invés de 1
for c in range(10,0,-1) - Iteração regressiva. Passo -1
"""

from Pacote1 import verifica

#------------------------------------
print("DESAFIO CONTAGEM REGRESSIVA")
import time
for cont in range(10,-1,-1):
    print(cont)
    time.sleep(1)
    if cont==0:
        print("FELIZ ANO NOVO!!!!")
print()


#------------------------------------
print("DESAFIO - TODOS NÚMERO PARES ENTRE 1 E 50")
for cont in range(2,51,2):
    print("{} é par".format(cont))
print()


#------------------------------------
print("DESAFIO - NÚMERO ÍMPARES MÚLTIPLO DE 3 ENTRE 1 E 500")
somatorio=0
for cont in range(1,500,2):
    if cont%3==0:#Se o contador for múltiplo de 3
        print(cont)
        somatorio+=cont
print("Soma total: {}".format(somatorio))
print()


#------------------------------------
print("DESAFIO TABUADA COM LAÇO FOR")
numero=verifica.verifica_int(input("Digite um número inteiro: "))
for cont in range(0,11):
    a=cont*numero
    print("{} x {} = {}".format(numero,cont,a))
print()


#------------------------------------
print("DESAFIO - SOMAR APENAS NÚMERO PARES")

soma=0
for cont in range(1,7):
    a=verifica.verifica_int(input("Digite o {}º número: ".format(cont)))
    if a%2==0:#SE NÚMERO FOR PAR
        soma+=a#SOMATÓRIO DOS NÚMEROS PARES
        print("{} é par!".format(a))
    else:
        print("{} é ímpar!".format(a))   
    print() 

print("Somando todos os números pares, temos o valor: {}".format(soma))
print()


#------------------------------------
print("DESAFIO - PROGRESSÃO ARITMÉTICA")
numero_atual=verifica.verifica_int(input("Qual o primeiro termo da PA: "))
razao=verifica.verifica_int(input("Qual a razao da PA: "))

for cont in range(1,11):
    print(numero_atual)
    numero_atual+=razao#incrementando o numero atual
print()


#------------------------------------
print("DESAFIO - NÚMERO PRIMO")
#divisível somente por ele mesmo e por um
numero=verifica.verifica_int(input("Digite um número inteiro: "))
for cont in range(2,numero):#PERCORRENDO TODOS OS NÚMEROS ENTRE 2 E O NÚMERO AVALIADO (-1)
    resto=numero%cont
    if resto==0:#se número for divisível por qualquer outro que não seja 1 ou ele mesmo
        print("É divisível por {}".format(cont))
        print("Não é primo")
        break
    if cont==numero-1:#Se eu tiver percorrido tudo sem quebrar a repetição
        print("É primo!")
print()


#------------------------------------
print("DESAFIO - PALÍNDROMO")
frase=input("Digite uma frase qualquer: ")
lista_frase=frase.split()
frase_nova=''.join(lista_frase)#gerado uma string da frase sem espaços
frase_nova2=frase_nova#copiando a string
#print(len(frase_nova))
contador=0
for letra in range(len(frase_nova),0,-1):#laço que percorre a string sem espaços, ao contrário
        #print(frase_nova[letra-1])
        if frase_nova[letra-1]==frase_nova2[contador]:#se a primeira letra for igual a última
                                                      #e assim sucessivamente
            #print("'{}' igual a '{}'".format(frase_nova[letra-1],frase_nova2[contador]))
            #print("Até aqui, tudo igual! ")
            if contador+1==len(frase_nova):#Se eu percorrer a frase toda sendo palíndromo
                print("A frase é um palíndromo!")
                break
            contador+=1 #incremento do contador
        else:#no caso de alguma letra ser diferente comparando as frases invertidas
            print("Não é palíndromo!")
            break
print()


#------------------------------------
print("DESAFIO - ANO DE NASCIMENTO DE 7 PESSOAS")
import datetime
a=datetime.datetime.now()
b=a.date()
ano_atual=verifica.verifica_int(b.strftime("%Y")) #isso tudo pra pegar o ano atual

maiore_idade=menor_idade=0
for cont in range(1,8):#SETE REPETIÇÕES
    ano=verifica.verifica_int(input("Digite o ano de nascimento da {}ª pessoa: ".format(cont)))
    if ano_atual-ano>=18:
        maiore_idade+=1
    else:
        menor_idade+=1

print("Menores de idade: {}\n"
      "Maiores de idade: {}".format(menor_idade,maiore_idade))
print()


#------------------------------------
print("DESAFIO - O MAIS GORDO E O MAIS MAGRO DENTRE 5")
maior=0#qualquer peso é maior que 0
menor=1000 #qualuqer peso humano é menor que 1000

for count in range(1,6):
    peso=verifica.verifica_float(input("Qual o peso da {}ª pessoa? ".format(count)))
    if peso>maior:
        maior=peso
    if peso<menor:
        menor=peso

print("Maior peso: {}\n"
      "Menor peso: {}".format(maior,menor))
print()


#------------------------------------
print("DESAFIO - NOME IDADE E SEXO DE 4 PESSOAS")
numero_pessoas=4
soma_idade=0      #inicialização de variáveis necessárias
mais_velho=0
mulheres_menosDe20=0

for count in range(1,numero_pessoas+1):
    nome=input("Nome da {}ª pessoas: ".format(count))
    idade = verifica.verifica_int(input("Idade da {}ª pessoas: ".format(count)))
    sexo = input("Sexo da {}ª pessoas(M/F) : ".format(count))
    sexo=sexo.upper()
    soma_idade+=idade#incrementando o somatório da idade
    if sexo=="M":
        if idade>mais_velho:#guardando a idade do homem mais velho
            mais_velho=idade
    if sexo=="F" and idade<20:
        mulheres_menosDe20+=1

media_idade=soma_idade/numero_pessoas
print("Média de idade do grupo: {}\n"
      "Idade do homem mais velho: {}\n"
      "Quantas mulheres com menos de 20 anos: {}".format(media_idade,mais_velho,mulheres_menosDe20))
print()