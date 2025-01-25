"""
LISTAS COMPOSTAS - listas dentro de listas
 teste=[]
 teste.append("Gustavo")
 teste.append(40)

 galera=[]
 galera.append(teste[:]) #UM ITEM DE GALERA RECEBE TODA A LISTA TESTE

#DECLARAÇÃO LISTA COMPOSTA
galera=[["Luciano",27], ["Cleber",30], ["Giovana",18], ["Gustavo",14]]

#LIMPAR LISTA
teste.clear()
"""

#---------------------------------------
print("DESAFIO - NOME E PESO")
pessoas=[]
pessoa=[]
continuar=True
peso_maior=0
peso_menor=1000
contador_pessoas=0

while continuar:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    pessoas.append(pessoa[:])#CÓPIA DE PESSOA ADICIONADA A PESSOAS
    contador_pessoas+=1
    pessoa.clear()#LIMPA PESSOA

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False

#PEGANDO A INFORMAÇÃO DE QUAL É O MAIOR PESO DA LISTA
for pessoa in pessoas:
    if pessoa[1]>=peso_maior:#pessoa[1] - é o peso, pessoa[0] é o nome
        peso_maior=pessoa[1]

#PEGANDO A INFORMAÇÃO DE QUAL É O MENOR PESO DA LISTA
for pessoa in pessoas:
    if pessoa[1]<=peso_menor:
        peso_menor=pessoa[1]

#MOSTRANDO OS RESULTADOS
print(f"Número de pessoas cadastradas: {contador_pessoas}\n")
print("Pessoas mais pesadas: ")
for pessoa in pessoas:
    if pessoa[1]==peso_maior:
        print(f"Nome: {pessoa[0]} - Peso: {pessoa[1]}")
print()

print("Pessoas mais leves: ")
for pessoa in pessoas:
    if pessoa[1]==peso_menor:
        print(f"Nome: {pessoa[0]} - Peso: {pessoa[1]}")
print()


#---------------------------------------
print("DESAFIO - LISTA COMPOSTA PARES E ÍMPARES")
#USAR SÓ UMA LISTA AO INVÉS DE 3
numeros=[[],[]]

for cont in range(1,8):#7 ENTRADAS DO USUÁRIO
    numero=int(input("Digite um número inteiro: "))
    if numero%2==0:#SE PAR, SALVO NA POS 0
        numeros[0].append(numero)
    else:#SE ÍMPAR, SALVO NA POS 1
        numeros[1].append(numero)

numeros[0].sort()#ORDENANDO
numeros[1].sort()#ORDENANDO

print(f"Números pares: {numeros[0]}\n"
      f"Números ímpares: {numeros[1]}")
print()


#---------------------------------------
print("DESAFIO - MATRIZ")
matriz=[]
linha=[]
soma_pares=soma_coluna3=soma_linha2=0


for c in range(0,3):
    for l in range(0,3):
        valor=int(input(f"Digite o valor para [{c}] [{l}]: "))
        linha.append(valor)#DENTRO DO LAÇO, SALVO 3 VALORES PARA A LISTA LINHA
        #SOMANDO VALORES PARES
        if valor%2==0:
            soma_pares+=valor
    matriz.append(linha[:])#APÓS TER 3 VALORES DE LINHA, INSIRO ELA NUMA POS DE MATRIZ
    linha.clear()#LIMPO A LINHA

#MOSTRANDO MATRIZ NA TELA
print("Matriz resultante: ")
for l in matriz:#PARA CADA ITEM DE MATRIZ, Q É UMA LINHA
    for i in l:
        print(f"[{i}]",end=" ")
    print()

#SOMA DE VALORES DA COLUNA 3
for l in matriz:#PARA CADA ITEM DA MATRIZ Q É UMA LINHA
    soma_coluna3+=l[2]#INCREMENTO COM O ÚLTIMO VALOR DA LINHA, Q É A TERCEIRA COLUNA

#SOMA DE VALORES DA LINHA 2
for i in matriz[1]:#PARA CADA ITEM DA SEGUNDA LINHA DA MATRIZ
    soma_linha2+=i

print(f"Soma de todos os valores pares: {soma_pares}\n"
      f"Soma da terceira coluna: {soma_coluna3}\n"
      f"Soma da segunda linha: {soma_linha2}\n")
print()


#---------------------------------------
print("DESAFIO - PALPITES DA MEGA SENA")
#6 números entre 1 e 60
#quantos jogos?
from random import sample #BIBLIOTECA Q GERA LISTA DE NÚMEROS SEM REPETIÇÕES
import time
palpites=[]

numero_jogos=int(input("Quantos jogos para gerar palpites: [Insira número]\n->> "))
for jogos in range(0,numero_jogos):#PARA CADA UM DOS JOGOS
    x=sample(range(1,61),6)#LISTA DE 6 NÚMEROS NÃO REPETIDOS ENTRE 1 E 60
    palpites.append(x[:])#ADICIONO O JOGO A LISTA DE PALPITES
    x.clear()#LIMPO A VARIÁVEL PARA CADA JOGO
#MOSTRANDO RESULTADOS NA TELA
for pos,jogo in enumerate(palpites):
    print(f"Jogo {pos+1}: {jogo}")
    time.sleep(1)
print()


#---------------------------------------
print("DESAFIO - ALUNO COM DUAS NOTAS")
sala=[]
alunoE_notas=[]
notas=[]
continuar=True
mostrar=True


while continuar:
    nome=str(input("Nome do aluno: "))
    nota1=float(input("Nota 1: [de 0 a 10]\n->> "))
    nota2=float(input("Nota 2: [de 0 a 10]\n->> "))
    #ADICIONANDO NOTAS À LISTA NOTAS, COM A MEDIA
    notas.append(nota1)
    notas.append(nota2)
    media=(nota1+nota2)/2
    notas.append(media)
    #ADICIONANDO NOME DO ALUNO E LISTA NOTAS À LISTA alunoEnotas
    alunoE_notas.append(nome)
    alunoE_notas.append(notas[:])
    #ADICIONANDO TODOS OS DADOS DO ALUNO À LISTA sala
    sala.append(alunoE_notas[:])
    #LIMPANDO LISTAS PARA PRÓXIMA REPETIÇÃO
    notas.clear()
    alunoE_notas.clear()

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False

#MOSTRANDO BOLETIM NA TELA
print(sala)

for pos1,aluno in enumerate(sala):#PARA CADA ITEM DA SALA
    print(f"ID Aluno: {pos1+1}\nNome:",aluno[0])#MOSTRO A POSIÇÃO INICIAL, QUE É O NOME
    for pos2,nota in enumerate(aluno[1]):#PARA CADA LISTA DE NOTAS EM CADA ALUNO
        if pos2==2:#SE FOR O DE POSIÇÃO DOIS, QUE É A MÉDIA, MOSTRO
            print("Média: ",nota)
    print("--------------------")

while mostrar:#ENQUANTO A PESSOA QUISER CONTINUAR MOSTRANDO NOTAS INDIVIDUAIS
    escolha=int(input("Mostrar notas de qual aluno? [Usar ID Alno]\n->> "))

    for pos3,aluno in enumerate(sala):
        if escolha==pos3+1:#PARA O ALUNO ESCOLHIDO PELO ID
            print(f"Aluno: {aluno[0]}",end="-/Notas: ")#MOTRO O NOME
            for pos4,nota in enumerate(aluno[1]):#PARA A LISTA DE NOTAS
                if pos4==0:#MOSTRO A PRIMEIRA
                    print(nota,end=" - ")
                if pos4==1:#E MOSTRO A SEGUNDA
                    print(nota,end=" ")
            print()

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op1 = input("Deseja continuar? [S/N]")
    op1 = op1.upper()
    while op1 not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op1 = input("Deseja continuar? [S/N]")
        op1 = op1.upper()
    if op1 in ["N", "NAO", "NÃO"]:
        mostrar = False
print()