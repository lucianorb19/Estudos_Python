"""
OPERADORES ARITMÉTICOS
Adição +
*Também pode ser usado para concatenar strings
Oi+Olá: OiOlá

Subtração -
Multiplicação *
*Também pode ser usado para multiplicar strings
Oi*3: OiOiOi

Divisão /
Potência ** ou função pow() - pow(2,3): 2 elevado ao cubo
Divisão Inteira //
Resto da divisão %
Raiz - X**(1/2): Raiz quadrada de X
       X**(1/3): Raiz cúbica de X

ORDEM DE PRESCEDÊNCIA
() parênteses
** exponenciação
* , /, //, % multiplicação, divisão, divisão inteira, resto da divisão
+, - soma e subtração
"""

from Pacote1 import verifica

#------------------------------------------------------------------
print('DESAFIO - ANTECESSOR, SUCESSOR, DOBRO, TRIPLO, RAIZ QUADRADA')
numero1=verifica.verifica_float(input("Digite um número: "))
sucessor1=numero1+1
antecessor1=numero1-1
dobro=numero1*2
triplo=numero1*3
raiz_quadrada=numero1**(1/2)
print("Sucessor: {}\n"
      "Antecessor: {}\n"
      "Dobro: {}\n"
      "Triplo: {}\n"
      "Raiz quadrada: {}".format(sucessor1,antecessor1,dobro,triplo,raiz_quadrada))
print()
      

#------------------------------------------------------------------
print('DESAFIO - SOMA DE DUAS NOTAS E SUA MÉDIA')
nota1=verifica.verifica_float(input("Digite a nota 1 do aluno: "))
nota2=verifica.verifica_float(input("Digite a nota 2 do aluno: "))
media1=(nota1+nota2)/2
print("Média do aluno: {}".format(media1))
print()


#------------------------------------------------------------------
print('DESAFIO - METROS EM CENTÍMETROS E MILÍMETROS')
metros1=verifica.verifica_float(input("Digite uma distância em metros: "))
centimetros1=metros1*100
milimetros=centimetros1*10
#print("A distância {}m em centímetros: {}. Em milímetros: {}".)
print("A distância {}m\n"
      "Em centímetros: {}cm\n"
      "Em milímetros: {}mm".format(metros1,centimetros1,milimetros))
print()


#------------------------------------------------------------------
print('DESAFIO TABUADA DE UM NÚMERO INTEIRO')
n1=verifica.verifica_int(input("Digite um número inteiro: "))
print("Tabuada de {}".format(n1))
print("{}x0 = {}\n"
      "{}x1 = {}\n"
      "{}x2 = {}\n"
      "{}x3 = {}\n"
      "{}x4 = {}\n"
      "{}x5 = {}\n"
      "{}x6 = {}\n"
      "{}x7 = {}\n"
      "{}x8 = {}\n"
      "{}x9 = {}\n".format(n1,n1*0,n1,n1*1,n1,n1*2,n1,n1*3,n1,n1*4,n1,n1*5
                           ,n1,n1*6,n1,n1*7,n1,n1*8,n1,n1*9))
print()

                           
#------------------------------------------------------------------
print('DESAFIO - QUANTOS DÓLARES CONSIGO COMPRAR COM REAIS')
reais=verifica.verifica_float(input("Quantos reais você tem na carteira? "))
dolares=reais/5.90
print("Com {} reais, você consegue comprar {} dólares!".format(reais,dolares))
print()


#------------------------------------------------------------------
print('DESAFIO - CALCULAR ÁREA DA PAREDE E QUANTIDADE DE TINTA")')
largura=verifica.verifica_float(input("Qual a largura da parede (em metros)? "))
altura=verifica.verifica_float(input("Qual a altura da parede (em metros)? "))
area_parede=altura*largura
tinta=area_parede/2 #cada litro de tinta pinta 2m quadrado
print("A área da parede é de {} metros quadrados!".format(area_parede))
print("Considerando que cada litro de tinta pinta 2 metros quadrados,\n"
      "a quantidade de tinta necessária para pinta essa parede será de "
      "{}L !".format(tinta))
print()


#------------------------------------------------------------------
print('DESAFIO - MOSTRAR PREÇO DO PRODUTO COM 5% DE DESCONTO")')
preco1=verifica.verifica_float(input("Digite o preço do produto: "))
preco2=preco1-(preco1*0.05)#preço atualizado com 5% de desconto
print("Valor com 5% de desconto: {}".format(preco2))
print()


#------------------------------------------------------------------
print('DESAFIO - AUMENTO DE 15% NO SALÁRIO')
salario1=verifica.verifica_float(input("Qual o salário atual do funcionário? "))
salario2=salario1+(salario1*0.25)#salário somado de 25%
print("Salário aumentado em 25%: {}".format(salario2))