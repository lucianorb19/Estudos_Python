"""
CONDICIONAL IF

if (condicao):
    codigo
else:
    codigo
"""

#---------------------------------------------------
print("DESAFIO - GERAR NÚMERO ALEATÓRIO ENTRE 0 E 5 "
      "PARA O USUÁRIO ACERTAR")
from random import randint
from random import random
print("Gerando número inteiro aleatório entre 0 e 5 !")
numero=randint(0,5)
tentativa = int(input("Qual número foi gerado pelo computador? "))
print("Número gerado pelo computador: {}".format(numero))
if numero==tentativa:
    print("Você acertou !")
else:
    print("Errou :(")
print()


#---------------------------------------------------
print("DESAFIO - MULTA DE TRÂNSITO ACIMA DE 80KM/H")
velocidade=float(input("Qual a velocidade do carro na via? "))
if velocidade>80:
    print("Velocidade acima da permitida! ")
    aux1=velocidade-80 #cálculo de quantos km estava acima de 80
    multa=7*aux1 #multa é de 7 reais para cada km acima
    print("Você foi multado em R${} pelos {}km/h acima da velocidade permitida! "
          "".format(multa,aux1))
else:
    print("Velocidade dentro da permitida \nTaca-le pau nesse carrinho, Marcos!")
print()


#---------------------------------------------------
print("DESAFIO - NÚMERO PAR OU ÍMPAR")
numero=int(input("Digite um número inteiro: "))
if (numero%2)==0:
    print("Número {} é par! ".format(numero))
else:
    print("Número {} é ímpar! ".format(numero))
print()


#---------------------------------------------------
print("Desafio - PREÇO DA PASSAGEM")
distancia=float(input("Qual a distância da viagem em km: "))
if distancia<=200:#caso a viagem seja de até 200km
    preco=0.5*distancia#cada km custa 0,5 reais
    print("Cada km da viagem custa R$0,5")
    print("Preço da viagem: R${}".format(preco))
else:#caso a viagem seja maior que 200km
    preco=0.45*distancia#cada km custa 0,45 reais
    print("Cada km da viagem custa R$0,45")
    print("Preço da viagem: R${:.2f}".format(preco))#{:.2f} limita o resultado a duas casas decimais
print()


#---------------------------------------------------
print("DESAFIO - ANO BISSEXTO")
#ano múltiplo de 4
#que não seja múltiplo de 100 (exceto os múltiplos de 400)
ano=int(input("Qual ano você quer verificar se foi/é/será bissexto? "))
if ano%4==0:#múltiplo de 4
    print("Múltiplo de 4")
    if ano%100==0:#múltiplo de 4 e 100
        print("É múltiplo de 100")
        if ano%400==0:#múltiplo de 4 e 100 e 400
            print("Múltiplo de 4")
            print("Bissexto")
        else: #múltiplo de 4 e 100 mas não 400
            print("Não é múltiplo de 4")
            print("Não é bissexto")
    else:#múltiplo de 4 mas não de 100
        print("Não é múltiplo de 100")
        print("Bissexto!")
else:#não é múltiplo de 4
    print("Não múltiplo de 4")
    print("Não é bissexto! ")
print()


#---------------------------------------------------
print("DESAFIO - QUAL O MAIOR E O MENOR NÚMERO")
maior=0
menor=0

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))

if n1>n2:
    print("N1 MAIOR QUE N2")
    if n1>n3:#n1 maior que os outros dois
        maior=n1
        if n2>n3:#com n1 maior, comparar os dois restantes
            menor=n3
        if n2==n3:
            menor=n2#ou n3, tanto faz
        if n3>n2:
            menor=n2
    if n1==n3:#n1 e n3 iguais
        maior=n1 #ou n3, mesma coisa
        menor=n2 #n1 e n3 iguais e n2 menor
    if n3>n1:#n1 maior que n2 e menor que n3
        maior=n3
        menor=n2

if n2>n1:
    print("N2 MAIOR QUE N1")
    if n2>n3:
        maior=n2
        if n1>n3:#com n2 maior, comparar os demais
            menor=n3
        if n1==n3:
            menor=n1#ou n3, mesma coisa
        else:#n3>n1
            menor=n1
    if n2==n3:#sendo n2 maior que n1, com n2 e n3 iguais
        maior=n2 #ou n3, mesma coisa
        menor=n1
    else:#n3>n2
        #sendo n1 menor que n2, e n2 menor q n3
        maior=n3
        menor=n1

if n1==n2:#n1==n2
    print("N1 IGUAL N2")
    if n1>n3:#n1 e n2 iguais, ambos maiores q n3
        print("N1 MAIOR QUE N3")
        maior=n1
        menor=n3
    if n1==n3:#todos iguais
        print("N1 IGUAL N3")
        maior=n1
        menor=n1
    if n3>n1:#n3>n1
        print("N3 MAIOR N3")
        #n1 e n2 iguais, com n3 maior que ambos
        maior=n3
        menor=n1

print("Maior: {}\n"
      "Menor: {}".format(maior,menor))


#---------------------------------------------------
print("DESAFIO - AUMENTO SALARIOS POR FAIXA")
salario=float(input("Qual valor do seu salário? "))

if salario>1250:
    salario=salario+(salario*0.1)#salario aumentado 10%
    print("Salário aumentado em 10%\n"
          "Valor do novo salário: {}".format(salario))
else:#se salário menor ou igual a 1250
    salario=salario+(salario*0.15)#salario aumentado 15%
    print("Salário aumentado em 15%\n"
          "Valor do novo salário: {}".format(salario))


#---------------------------------------------------
print("DESAFIO - ESSAS TRÊS RETAS FORMAM UM TRIÂNGULO ?")
#A condição para que 3 retas formem um triâgulo é que
#um de seus lados deve ser maior que o valor absoluto da diferença dos outros dois
#e menor que a soma dos outros dois

a=float(input("Digite o comprimento da reta1: "))
b=float(input("Digite o comprimento da reta2: "))
c=float(input("Digite o comprimento da reta3: "))

              #a em relação bc
if a>abs(b-c):#se a maior que o valor absoluto da diferença dos outros dois
    if a<(b+c): #e se a menor que a soma dos outros dois
        if b>abs(a-c):#b em relação ac
            if b<(a+c):
                if c>abs(a-b):#c em relação ab
                    if c<(a+b):
                        print("Triângulo!")
                    else:
                        print("NÃO TRIÂNGULO!")
                else:
                    print("NÃO TRIÂNGULO!")
            else:
                print("NÃO TRIÂNGULO!")
        else:
            print("NÃO TRIÂNGULO!")
    else:
        print("NÃO TRIÂNGULO!")
else:
    print("NÃO TRIÂNGULO!")
print()