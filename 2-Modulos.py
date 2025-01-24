"""
IMPORTAÇÃO DE MÓDULOS NO PYTHON

import + nome biblioteca
ou
from + nome biblioteca + import + nome função,nome função,nome função....
"""
#---------------------------------------------------
print('EXEMPLO')
#import math
from math import sqrt
numero=float(input("Digite um número: "))
#raiz = math.sqrt(numero)
raiz = sqrt(numero)
print("A raiz de {} é {:.2f}".format(numero,raiz))
print()


#---------------------------------------------------
print('MOSTRAR A PORÇÃO INTEIRA DE UM NÚMERO')
import math
num=float(input("Digite um número: "))
num1=math.trunc(num)
print("A porção inteira de {} é: {}".format(num,num1))


#---------------------------------------------------
print('TEOREMA DE PITÁGORAS')
# o quadrado da hipotenusa é igual a soma do quadrado dos catetos
#h2 = ad2 + opo2
#import math
cateto_ad=float(input("Qual o valor do cateto adjacente? "))
cateto_opo=float(input("Qual o valor do cateto oposto? "))
aux=(pow(cateto_opo,2))+(pow(cateto_ad,2))#soma do quadrado dos catetos
hipo=math.sqrt(aux)#hipotenusa é a raiz da soma dos quadrados dos catetos
print("Hipotenusa resultante: {}".format(hipo))


#---------------------------------------------------
#import math
print('SENO, COSSENO E TANGENTE DE UM ÂNGULO')
angulo1=float(input("Digite o valor do ângulo em graus(de 1 a 179): "))
#como as funções calculam em radianos, é preciso converter o valor
#do ângulo de graus para radianos
angulo = math.radians(angulo1)
cosseno=math.cos(angulo)
seno=math.sin(angulo)
tangente=math.tan(angulo)

print("Cosseno: {}\n"
      "Seno: {}\n"
      "Tangente: {}\n".format(cosseno,seno,tangente))


#---------------------------------------------------
print('DESAFIO LER O NOME DE 4 ALUNOS E MOSTRAR UM ALEATORIAMENTE')
import random
alunos=["carlos","luciano","diogo","mateus"]
print("Os alunos são Carlos, Luciano, Digo e Mateus !")
escolhido=random.choice(alunos)#escolhendo um item da sequencia alunos
print("O aluno sorteado foi {}".format(escolhido))


#---------------------------------------------------
print('DESAFIO SORTEAR A ORDEM DE APRESENTAÇÃO DOS 4 ALUNOS')
#import random
alunos=["luciano","mateus","diogo","carlos"]
print("Os alunos são {}".format(alunos))
random.shuffle(alunos)
print("A lista de apresentação sorteada aleatoriamente será:\n"
      "{}".format(alunos))


#---------------------------------------------------
#PROXY IMPEDIU import :(
#DESAFIO ABRIR E REPRODUZIR UM ARQUIVO MP3
"""
from pygame import mixer
mixer.init()
mixer.music.load("CAMINHO")
mixer.music.set_volume(0.5)
mixer.music.play()
"""