"""
if(condicao1):
    codigo
elif(condicao2):
    codigo
else:
    codigo

#EXEMPLO
if nome=="luciano":
    print("nome bonito!")
elif nome=="clebervaldo":
    print("nome feio")
elif nome=="joao" or nome=="pedro":
    print("que nome comum")
elif nome in "claudio gustavo anderson":
    print("Nome é claudio ou gustavo ou anderson")
else:
    print("Chegamos no else!")
"""

from Pacote1 import verifica

#----------------------------------------------------------
print("DESAFIO - FINANCIAMENTO IMOBILIÁRIO")
#valor da mensalidade não pode ser maior que 30% do salário
valor_casa=verifica.verifica_float(input("Qual o valor da casa a ser financiada? "))
salario=verifica.verifica_float(input("Qual o valor de seu salário? "))
prazo_anos=verifica.verifica_int(input("Em quantos anos você pretende pagar a casa? "))

mensalidade=valor_casa/(prazo_anos*12)# valor da mensalidade dividindo
                                      #o valor da casa pelo número de meses do prazo de compra
if mensalidade>(salario*0.3):
    print("Empréstimo negado!")
    print("O valor de sua mensalidade (R$ {:.2f}) é maior que "
          "30% do seu salário (R$ {:.2f}) !".format(mensalidade,(salario*0.3)))
else:#mensalidade menor ou igual a 30% do salário
    print("Empréstimo aprovado!")
    print("O valor de sua mensalidade (R$ {:.2f}) é menor ou igual a "
          "30% de seu salário (R$ {:.2f})".format(mensalidade,(salario*0.3)))
print()


#----------------------------------------------------------
print("DESAFIO - CONVERSÃO DE BASE NUMÉRICA")
numero=verifica.verifica_int(input("Digite um número inteiro natural: "))
print("CONVERSÃO DE DECIMAL PARA:\n"
      "1- Binário\n"
      "2- Octal\n"
      "3- Hexadecimal")
escolha=verifica.verifica_int(input("-> "))

#USANDO A FUNÇÃO bin, oct ou hex, O RESULTADO É UMA STRING
#CUJOS PRIMEIROS DOIS CARACTÉRES NÃO FAZEM PARTE
#DA SUA REPRESENTAÇÃO BINÁRIA, OCTAL OU HEXADECIMAL, LOGO SÃO RETIRADOS
if escolha==1:
    n_binario=bin(numero)
    print("{} em binário: {}".format(numero,n_binario[2:]))
elif escolha==2:
    n_octal=oct(numero)
    print("{} em octal: {}".format(numero,n_octal[2:]))
elif escolha==3:
    n_hexadecimal=hex(numero)
    print("{} em hexadecimal: {}".format(numero,n_hexadecimal[2:]))
else:
    print("Entrada inválida :(")
print()


#----------------------------------------------------------
print("DESAFIO - NÚMERO MAIOR OU MENOR")
numero1=verifica.verifica_int(input("Digite um número inteiro qualquer: "))
numero2=verifica.verifica_int(input("Digite outro número inteiro qualquer: "))
maior=menor=0

if numero1>numero2:
    print("O primeiro número é maior! ")
elif numero2>numero1:
    print("O segundo número é maior! ")
else:#números iguais
    print("Não existe valor maior, os dois são iguais! ")
print()


#----------------------------------------------------------
print("DESAFIO - ALISTAMENTO MILITAR")
import datetime
a=datetime.datetime.now()
b=a.date()
ano_atual=verifica.verifica_int(b.strftime("%Y")) #isso tudo pra pegar o ano atual

ano_nascimento=verifica.verifica_int(input("Em qual ano você nasceu? "))
idade=ano_atual-ano_nascimento #cálculo da idade

diferenca=abs(18-idade)
if idade<18:
    print("Ainda não é hora de se alistar!")
    print("Faltam {} anos para seu alistamento!".format(diferenca))
elif idade==18:
    print("Este é seu ano de alistamento no serviço militar!")
else:#idade > 18
    print("Você já passou do ano de alistamento militar!")
    print("Sua época de alistamento foi há {} anos atrás".format(diferenca))
print()


#----------------------------------------------------------
print("DESAFIO - MÉDIA DE NOTAS - NOTAS DE 0 A 10")

nota1=verifica.verifica_float(input("Qual foi sua primeira nota? "))
nota2=verifica.verifica_float(input("Qual foi sua segunda nota? "))
media=(nota1+nota2)/2
print(media)

if media<5:
    print("Reprovado")
elif media>=5 and media<=6.9:
    print("Em recuperação")
else:#media >=7
    print("Aprovado! ")
print()


#----------------------------------------------------------
print("DESAFIO - CATEGORIA DE NATAÇÃO")
import datetime
a=datetime.datetime.now()
b=a.date()
ano_atual=verifica.verifica_int(b.strftime("%Y")) #isso tudo pra pegar o ano atual
ano_nascimento=verifica.verifica_int(input("Em qual ano você nasceu? "))
idade=ano_atual-ano_nascimento

if idade<=9:
    print("Categoria Mirim!")
elif idade>9 and idade<=14:
    print("Categoria Infantil!")
elif idade>14 and idade<=19:
    print("Categoria Junior!")
elif idade>19 and idade<=20:
    print("Categoria Sênior!")
else:#mais velho que 20
    print("Categoria Master!")
print()


#----------------------------------------------------------
print("DESAFIO - ESSAS TRÊS RETAS FORMAM UM TRIÂNGULO ?\n"
      "+ QUAL TIPO DE TRIÂNGULO")
#A condição para que 3 retas formem um triâgulo é que
#um de seus lados deve ser maior que o valor absoluto da diferença dos outros dois
#e menor que a soma dos outros dois

a=verifica.verifica_float(input("Digite o comprimento da reta1: "))
b=verifica.verifica_float(input("Digite o comprimento da reta2: "))
c=verifica.verifica_float(input("Digite o comprimento da reta3: "))

              #a em relação bc
if a>abs(b-c):#se a maior que o valor absoluto da diferença dos outros dois
    if a<(b+c): #e se a menor que a soma dos outros dois
        if b>abs(a-c):#b em relação ac
            if b<(a+c):
                if c>abs(a-b):#c em relação ab
                    if c<(a+b):
                        #print("Triângulo!")
                        #AGORA DEFINIR QUAL TIPO DE TRIÂNGULO
                        if a==b and b==c:
                            print("Triângulo Equilátero! ")
                        elif a==b and b!=c or a==c and c!=b or b==c and c!=a:
                            print("Triângulo Isósceles! ")
                        elif a!=b and b!=c:
                            print("Triângulo Escaleno! ")
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


#----------------------------------------------------------
print("DESAFIO - IMC")
altura=verifica.verifica_float(input("Qual sua altura (m) ?"))
peso=verifica.verifica_float(input("Qual seu peso (kg) ?"))
imc=peso/altura**2#peso / altura ao quadrado
print(imc)

if imc<18.5:
    print("Abaixo do peso!")
elif imc>=18.5 and imc<25:
    print("Peso ideal!")
elif imc>=25 and imc<30:
    print("Sobrepeso!")
elif imc>=30 and imc<40:
    print("Obesidade!")
else:#imc>=40
    print("Obesidade mórbida! ")
print()


#----------------------------------------------------------
print("DESAFIO - CONDIÇÕES DE PAGAMENTO")
preco_normal=verifica.verifica_float(input("Qual o preço normal do produto? "))

op=verifica.verifica_int(input("Qual vai ser a forma de pagamento?\n"
             "1 - À vista em dinheiro (10% de desconto)\n"
             "2 - À vista no cartão (5% de desconto)\n"
             "3 - Até 2x no cartão (preço normal)\n"
             "4 - 3x ou mais no cartão (20% de juros)\n"
             "->> "))

if op==1:
    preco_normal=preco_normal-(preco_normal*0.1)#10% de desconto
elif op==2:
    preco_normal=preco_normal-(preco_normal * 0.05)#5% de desconto
elif op==3:#não faz nada
    print("Preço continua o mesmo")
elif op==4:
    preco_normal = preco_normal+(preco_normal * 0.2)#20% de juros

print("Valor do produto: {}".format(preco_normal))
print()


#----------------------------------------------------------
print("DESAFIO JOKENPÔ")
from random import randint
opP=verifica.verifica_int(input("Qual sua jogada?\n"
      "1-Pedra\n"
      "2-Papel\n"
      "3-Tesoura\n"
      "->>"))
opC=randint(1,3)#opção de 1 a 3 escolhida pelo computador
if opC==1:
    print("Computador jogou: Pedra")
elif opC==2:
    print("Computador jogou: Papel")
elif opC==3:
    print('Computador jogou:Tesoura')

if opP==1 and opC==1 or opP==2 and opC==2 or opP==3 and opC==3:#CASOS DE EMPATE
    print("Empate!")
elif opP==2 and opC==1 or opP==3 and opC==2 or opP==1 and opC==3:#CASOS DE VITÓRIA PESSOA
    print("Vitória sua! ")
elif opP==3 and opC==1 or opP==1 and opC==2 or opP==2 and opC==3:
    print("Vitória do computador! ")
print()
