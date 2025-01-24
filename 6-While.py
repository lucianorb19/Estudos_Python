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