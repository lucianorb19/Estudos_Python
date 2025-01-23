""""
TIPOS PRIMITIVOS

int - inteiros
float - reais
bool - boleano True ou False
str - string, entre aspas

Funções aplicadas às entradas da variável 'x'
x.isnumeric - Retorna True se o número puder ser convertido em int/float.
x.isalpha - retorna True se a entrada puder ser convertida em string puro (somente letras)
x.isalphanumeric - retorna True se a entrada puder ser convertida em uma variável alfanumérica (número e letras)
x.isupper - Se há somente letras maiúsculas
x.islower - Se há somente letras minúsculas
dentres outros....
"""


#CASOS DE USO DO PRINT
nome=input("Qual seu nome? ")
print("Seu nome é {}".format(nome)) #- Caso típico
print("Seu nome é {:10}".format(nome)) #- Mostra a variável limitada a 10 espaços
print("Seu nome é {:>10}".format(nome))#- Caso anterior, mas alinhado à direita
print("Seu nome é {:<10}".format(nome))#- Alinhado à esquerda
print("Seu nome é {:^10}".format(nome))#- Alinhado no meio
print("Seu nome é {:=^10}".format(nome)) #- Alinhado ao meio, em 10 espaços, preenchendo os vazios com '='
print()

#------------------------------------------
print("DESAFIO - SOMA DE DOIS NÚMEROS")
n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
print('Tipo da variável n1:',type(n1))
print('Tipo da variável n2:',type(n2))
print('')
resultado=n1+n2
#print('A soma entre',n1,' e ',n2,' é',resultado,'!')
print('A soma entre {} e {} é {}!'.format(n1,n2,resultado))
print()


#------------------------------------------
print("DESAFIO - INFORMAÇÕES DA ENTRADA")
a=input("Digite algo: ")
print("Informações sobre {}".format(a))
print("{} é alfanumérico: {}".format(a,a.isalnum()))
print("{} é 'alfabético': {}".format(a,a.isalpha()))
print("{} é minúsculo: {}".format(a,a.islower()))
print("{} é numérico: {}".format(a,a.isnumeric()))
print("{} é maiúsculo: {}".format(a,a.isupper()))
print()