"""
while(condição):
    codigo


#EXEMPLO
op=0
while op==0:
    sexo=input("Qual o sexo da pessoa? [M/F]\n->> ")
    sexo=sexo.upper()
    if sexo=="M" or sexo=="F":
        op=1
    else:
        print("Opção inválida! Tente novamente.")

print("Sexo: {}".format(sexo))
"""


#----------------------------------------------------
print("DESAFIO - GERAR NÚMERO ALEATÓRIO ENTRE 0 E 5 "
      "PARA O USUÁRIO ACERTAR")
from random import randint
print("Gerando número inteiro aleatório entre 0 e 5 !")
numero=randint(0,5)

tentativa=-1
while tentativa!=numero:#enquanto a  pessoa não digitar um número igual ao gerado aleatoriamente
    tentativa = int(input("Qual número foi gerado pelo computador?\n->> "))
    #print("Número gerado pelo computador: {}".format(numero))
    if numero==tentativa:
        print("Você acertou!")
    else:
        print("Errou! Tente novamente.")
print()


#----------------------------------------------------
print("DESAFIO - MENU DE OPÇÕES PARA OPERAÇÕES")
valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
op=-1
while op!=5:
    op=int(input("MENU DE OPÇÕES\n"
          "[1] - SOMAR\n"
          "[2] - MULTIPLICAR\n"
          "[3] - QUAL MAIOR\n"
          "[4] - NOVOS NÚMEROS\n"
          "[5] - SAIR DO PROGRAMA\n->>"))

    if op==1:
        soma=valor1+valor2
        print("Soma dos valores: {}\n".format(soma))
    elif op==2:
        multi=valor1*valor2
        print("Multiplicação dos valores: {}\n".format(multi))
    elif op==3:
        maior=0
        if valor1>valor2:
            maior=valor1
        if valor2>valor1:
            maior=valor2
        print("Maior número: {}\n".format(maior))
    elif op==4:
        valor1=float(input("Digite o novo primeiro valor: "))
        valor2=float(input("Digite o novo segundo valor: "))
    #if op!=1 and op!=2 and op!=3 and op!=4 and op!=5:#entrada errado do usuário
    if op not in [1,2,3,4,5]:
        print("Opção insdisponível! Tente novamente\n")
print()


#----------------------------------------------------
print("DESAFIO - FATORIAL")
num=int(input("Digite um número inteiro natural: "))

resultado=1
contador=num
while contador!=1:
    resultado*=contador
    contador-=1

if num==1:
    resultado=1

print("Fatorial de {} é {}".format(num,resultado))
print()


#----------------------------------------------------
print("DESAFIO - PROGRESSÃO ARITMÉTICA COM WHILE")
numero=int(input("Qual o primeiro termo da PA: "))
razao=int(input("Qual a razao da PA: "))

print("Mostrando os primeiros 10 números da PA:")
contador=1
while contador<=10:
    print(numero)
    numero+=razao  # incrementando o numero atual
    contador+=1

ultimo=numero #salvando o último termo da PA

op=-1
while op!=0:
    op=repet=int(input("Quantos termos a mais para a PA? [0 PARA SAIR]"))
    contador = 1
    while contador<=repet:
        print(ultimo)
        ultimo+=razao
        contador+=1
print()


#----------------------------------------------------
print("DESAFIO - SEQUENCIA DE FIBONACCI")
digitos=int(input("Quantos números da sequência de fibonacci serão mostrados na tela? "))

contador=0
ultimo=1
penultimo=0
print("0 -> 1 -> ",end="")
while contador<=digitos:
    proximo=ultimo+penultimo
    print(proximo,"->",end=" ")
    penultimo = ultimo
    ultimo=proximo
    contador+=1
print()


#----------------------------------------------------
print("DESAFIO - LER NÚMERO E SÓ PARAR AO LER 999")
numero=soma=contador=0
while numero!=999:
    numero=int(input("Digite um número qualquer: "))
    if numero!=999:
        soma+=numero
        contador+=1
print("Soma dos valores digitados (exceto 999): {}\n"
      "Quantos número foram digitados: {}".format(soma,contador))
print()


#----------------------------------------------------
print("DESAFIO - LER NÚMERO E MOSTRAR MÉDIA")
soma=op=numero=media=contador=0
maior=0
menor=1000

while op!=1:
    numero=int(input("Digite um número inteiro qualquer: "))
    soma+=numero
    contador+=1
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
    continuar=input("Deseja continuar? [S/N]\n->> ")
    continuar=continuar.upper()
    if continuar=="N" or continuar=="NAO" or continuar=="NÃO":
        op=1

media=soma/contador
print("Média dos número digitados: {}\n"
      "Menor valor digitado: {}\n"
      "Maior valor digitado: {}".format(media,menor,maior))
print()


#---------------------------------------------
print("DESAFIO - TABUADA DE VÁRIOS NÚMEROS")
numero=0
while numero>=0:
    numero = int(input("Tabuada de qual número? (-1 para sair)\n--> "))
    if numero>=0:
        for cont in range(1,11):
            print("{} x {} = {}".format(numero,cont,(cont*numero)))
        print()
print()


#---------------------------------------------
print("DESAFIO - PAR OU ÍMPAR")
import time
import random
vitoria=True
contador_vitoria=soma=0

while vitoria==True:#ENQUANTO O JOGADOR GANHAR
    op_jogador=input("Você quer jogar par ou ímpar? ")
    op_jogador=op_jogador.upper()
    #LAÇO PARA GARANTIR UM ENTRADA PAR OU IMPAR
    while op_jogador not in ['PAR','P','IMPAR','ÍMPAR','I']:
        print("Entrada inválida! Tente novamente.")
        print()
        op_jogador=input("Você quer jogar par ou ímpar? ")
        op_jogador=op_jogador.upper()

    #CASO O JOGADOR JOGUE PAR
    if op_jogador=="PAR" or op_jogador=="P":
        op_computador="IMPAR"
        op_jogador="PAR"
        #LAÇO PARA GARANTIR UMA ENTRADA INTEIRA PAR
        numero_pessoa = int(input("Digite um número inteiro par: "))
        while numero_pessoa%2!=0:#enquanto a pessoa não digitar um número par
            numero_pessoa = int(input("Você não digitou um número par.\nDigite novamente: "))

    #CASO O JOGADOR JOGUE ÍMPAR
    if op_jogador=="IMPAR" or op_jogador=="ÍMPAR" or op_jogador=="I":
        op_computador="PAR"
        op_jogador="IMPAR"
        #LAÇO PARA GARANTIR UMA ENTRADA INTEIRA ÍMPAR
        numero_pessoa = int(input("Digite um número inteiro ímpar: "))
        while numero_pessoa % 2 == 0:  # enquanto a pessoa não digitar um número ímpar
            numero_pessoa = int(input("Você não digitou um número ímpar.\nDigite novamente: "))



    print("Computador jogou.... ",end="")
    time.sleep(1)
    #COMPUTADOR GERA UM NÚMERO INTEIRO ALEATÓRIO ENTRE 0 E 1000
    numero_computador=int(random.randint(0,1000))
    print(numero_computador)
    soma=numero_pessoa+numero_computador
    print("Somando os valores temos -> {}".format(soma),end=" ")

    #SE O JOGADOR TIVER ESCOLHIDO PAR
    if op_jogador=="PAR":
        if soma%2==0:#soma par
            contador_vitoria += 1#INCREMENTO CONTADOR VITÓRIA
            print("Deu par! Você ganhou!")
        elif soma%2!=0:#soma impar
            print("Deu ímpar! Computador ganhou!")
            vitoria = False#CONDIÇÃO PARA SAÍDA DO LAÇO

    #SE O JOGADOR TIVER ESCOLHIDO ÍMPAR
    elif op_jogador=="IMPAR":
        if soma%2==0:#soma par
            print("Deu par! Computador ganhou!")
            vitoria = False
        elif soma%2!=0:#soma impar
            contador_vitoria += 1
            print("Deu ímpar! Você ganhou!")

print("\nFim de jogo!\nVocê ganhou {} rodadas".format(contador_vitoria))
print()


#---------------------------------------------
print("DESAFIO - IDADE E SEXO DE VÁRIAS PESSOAS")
continuar=True
cont=1
maior_18=homens=mulheres_menos20=0
#ENQUANTO A PESSOA ESCOLHER CONTINUAR
while continuar==True:
    #ENTRADA DA IDADE
    idade=int(input("Idade da pessoa {}: ".format(cont)))

    #ENTRADA DO SEXO COM VERIFICAÇÃO
    sexo=input("Sexo da pessoa {} [F/M]: ".format(cont))
    sexo=sexo.upper()
    #SE HOMEM
    while sexo not in ["M","MASCULINO","HOMEM","F","FEMININO","MULHER"]:
        print("Entrada inválida. Digite novamente!")
        sexo = input("Sexo da pessoa {} [F/M]: ".format(cont))
        sexo = sexo.upper()
    if sexo in ["M", "MASCULINO", "HOMEM"]:
        homens+=1

    #SE MAIOR DE IDADE
    if idade>18:
        maior_18+=1

    #QUANTAS MULHERES MAIS DE 20 ANOS
    if sexo=="F" or sexo=="FEMININO" or sexo=="MULHER":
        if idade<20:
            mulheres_menos20+=1
    
    #OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op=input("Deseja continuar? [S/N]")
    op=op.upper()
    while op not in ["S","N","SIM","NÃO","NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op=="N" or op=="NÃO" or op=="NAO":
        continuar=False
    cont+=1#INCREMENTO CONTADOR DE REPETIÇÕES DO LAÇO

print()
print("Número de pessoas com mais de 18 anos: {}\n"
      "Número de homens cadastrados: {}\n"
      "Número de mulheres com menos de 20 anos: {}".format(maior_18,homens,mulheres_menos20))
print()


#---------------------------------------------
print("DESAFIO - PREÇO E NOME DE VÁRIOS PRODUTOS")
continuar=True
cont=1
total_compra=produtos_maior_que_mil=0
#A VARIÁVEL QUE GUARDA O VALOR DO PRODUTO DE MENOR VALOR É INICIALIZADA COM
#UM NÚMERO GRANDE, PRA QUE NA COMPARAÇÃO, ELA POSSA ASSUMIR UM NÚMERO PEQUENO
mais_barato=1000000
nome_mais_barato=""

while continuar==True:
    nome=input("Nome do {}º produto: ".format(cont))
    valor=float(input("Preço do {}º produto: ".format(cont)))
    #TOTAL DA COMPRA INCREMENTADO PELO VALOR DO ITEM
    total_compra+=valor
    #INCREMENTO CONTADOR DE PRODUTOS MAIS CAROS QUE 1000
    if valor>1000:
        produtos_maior_que_mil+=1
    #SE FOR O PRODUTO MAIS BARATO, SALVO O NOME
    if valor<mais_barato:
        mais_barato=valor
        nome_mais_barato=nome

    #OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO","NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N","NAO","NÃO"]:
        continuar = False
    cont += 1  # INCREMENTO CONTADOR DE REPETIÇÕES DO LAÇO

#MOSTRANDO NA TELA OS RESULTADOS
print("Total gasto na compra: {}\n"
      "Quantos produtos custam mais que R$1.000,00:  {}\n"
      "Nome do produto mais barato:  {}".format(total_compra,produtos_maior_que_mil,nome_mais_barato))
print()


#---------------------------------------------
print("DESAFIO - CAIXA ELETRÔNIOCO EMITINDO CÉDULAS")
saque=int(input("Qual o valor do saque? "))
#INICIALIZAÇÃO DAS VARIÁVEIS
cedulas_100=cedulas_50=cedulas_20=cedulas_10=cedulas_1=0

#ENQUANTO NÃO TIVER EMITIDO TODO O VALOR DO SAQUE
while saque!=0:
    #SE O VALOR FOR DIVISÍVEL POR 100
    if (saque/100)>=1:
        #NÚMERO DE CÉDULAS DE 100 É O VALOR INTEIRO DA DIVISÃO DO SAQUE POR 100
        cedulas_100 = int(saque / 100)
        #VARIÁVEL SAQUE RECEBE O RESTO DA DIVISÃO POR 100
        saque = saque % 100
        print("Cédulas R$100: {}".format(cedulas_100))
    #PARA AS DEMAIS CÉDULAS, DADO O NOVO VALOR DA VARIÁVEL SAQUE, SE REPETE O PROCEDIMENTO
    elif (saque/50)>=1:
        cedulas_50 = int(saque / 50)
        saque = saque % 50
        print("Cédulas R$50: {}".format(cedulas_50))
    elif (saque/20)>=1:
        cedulas_20 = int(saque / 20)
        saque = saque % 20
        print("Cédulas R$20: {}".format(cedulas_20))
    elif (saque/10)>=1:
        cedulas_10 = int(saque / 10)
        saque = saque % 10
        print("Cédulas R$10: {}".format(cedulas_10))
    else:
        cedulas_1 = saque
        print("Cédulas R$1: {}".format(cedulas_1))
        #CASO CHEGUE NAS CÉDULAS DE 1, SAI DO LAÇO
        break