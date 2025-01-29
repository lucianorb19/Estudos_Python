"""
DECLARAÇÃO DE DICIONÁRIOS
dados=dict()
dados={}
dados={'nome':'Luciano','idade':25}

#ADICIONAR UMA CHAVE sexo ao dicionário
dados['sexo']='M'  #ADICIONAR A CHAVE SEXO AO FINAL DO DICIONÁRIO, JÁ COM O VALOR M

#DELETAR CHAVE
del dados['idade']  #RETIRA A CHAVE idade DO DICIONÁRIO

#PRINT PARA DICIONÁRIOS
pessoa={"Nome":"Luciano","Sexo":"M","Idade":27}
print(pessoa["Nome"])
print(f"{pessoa["Nome"]} tem {pessoa["Idade"]} anos")

#MOSTRAR OS VALORES DO DICIONÁRIO
print(dados.values())  #MOSTRA O CONTEÚDO
#OU
for v in dados.values():
    print(v)

#MOSTRAR AS CHAVES DO DICIONÁRIO
print(dados.keys())  #MOSTRA A ESTRUTURA
#ou
for k in dados.keys():
    print(k)

MOTRAR TUDO DO DICIONÁRIO
print(dados.items())  #MOSTRA O CONTEÚDO E ESTRUTURA

LAÇO FOR PARA DICIONÁRIO
for chave,valor in dados.items():
    print(f"{chave}: {valor}") #MOSTRA A ESTRUTURA COMPLETA DE CADA ITEM DO DICIONÁRIO

ATRIBUIÇÃO DE UM DICIONÁRIO PARA OUTRA ESTRUTURA
brasil=list()
estado=dict()

estado["UF"]="Minas Gerais"
estado["Sigla"]="MG"
brasil.append(estado.copy())
"""

from Pacote1 import verifica


#---------------------------------------------------------
print("DESAFIO - NOME NOTA E SITUAÇÃO DO ALUNO")
aluno=dict()

aluno["nome"]=str(input("Nome do aluno: "))
aluno["media"]=verifica.verifica_float(input(f"Media de {aluno["nome"]}: "))
if aluno["media"]<7:
    aluno["situacao_aluno"]="Reprovado"
else:
    aluno["situacao_aluno"]="Aprovado"
print()
for chave,valor in aluno.items():
    print(f"{chave}: {valor}")
print()


#---------------------------------------------------------
print("DESAFIO - JOGAR DADOS E COLOCAR EM ORDEM")
from random import randint
from operator import itemgetter#para pegar a chave do dicionário
jogadores=dict()
jogadores_ordenados=list()
maior=0

#PREENCHENDO O DICIONÁRIO - CADA CAMPO É UM JOGADOR
jogadores={'Jogador 1': randint(1,6),
           'Jogador 2': randint(1,6),
           'Jogador 3': randint(1,6),
           'Jogador 4': randint(1,6)}

#MOSTRANDO OS JOGADORES COM SEUS DADOS JOGADOS
for chave, valor in jogadores.items():
    print(f"{chave} : {valor}")
print()

#ORDENANDO O DICIONÁRIO EM UMA LISTA - MÉTODO SORTED GERA LISTA
#AQUI FOI USADO O OPERATOR PARA ORDENAR O DICIONÁRIO USANDO O VALOR DE CADA CHAVE
#itemgetter(1) - Significa que ordena pelo valor da chave
#itemgetter(0) - Significaria que ordena pela própria chave
jogadores_ordenados=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print(jogadores_ordenados)
print()

#COMO O RESULTADO É UMA LISTA, CONTENDO TUPLAS, MOSTRAMOS ASSIM
print("RANKING DOS JOGADORES")
for pos, valor in enumerate(jogadores_ordenados):
    print(f"{pos+1}º lugar: {valor[0]} - {valor[1]} pontos")
print()


#---------------------------------------------------------
#FALTA CONSIDERAR APOSENTADORIA POR TEMPO DE SERVIÇO NA IDADE MÍNIMA
print("DESAFIO - DADOS CARTEIRA DE TRABALHO")
from datetime import datetime #BIBLIOTECA PARA TRATAR ANO NASCIMENTO
dados_pessoa=dict()

#PREENCHENDO O DICIONÁRIOS COM AS ENTRADAS DO USUÁRIO
dados_pessoa["Nome"]=str(input("Nome: "))
sexo=str(input("Sexo: "))
sexo=sexo.upper()
while sexo not in ["F","MULHER","FEMININO","M","HOMEM","MASCULINO"]:
    print("Entrada inválida! Tente novamente.")
    sexo = str(input("Sexo: "))
    sexo.upper()
dados_pessoa["Sexo"]=sexo

dados_pessoa["Ano de Nascimento"]=verifica.verifica_int(input("Ano de nascimento: "))
#DEFININDO IDADE PELO ANO DE NASCIMENTO
#a=datetime.datetime.now()
#b=a.date()
#ano_atual=int(b.strftime("%Y")) #isso tudo pra pegar o ano atual
ano_atual=datetime.now().year
idade=ano_atual-dados_pessoa["Ano de Nascimento"]
dados_pessoa["Idade"]=idade

#SE CARTEIRA DE TRABALHO FOR DIFERENTE DE ZERO, DICIONÁRIO RECEBE TAMBÉM ANO DE CONTRATAÇÃO
#E SALÁRIO E COM QUANTOS ANOS A PESSOA IRÁ SE APOSENTAR
carteira_detrabalho=verifica.verifica_int(input("Possui carteira de trabalho assinada: [0-NAO/1-SIM]\n->> "))
while carteira_detrabalho not in [0,1]:
    print("Entrada inválida. Tente novamente!")
    carteira_detrabalho = verifica.verifica_int(input("Possui carteira de trabalho assinada: [0-NAO/1-SIM]\n->>  "))
dados_pessoa["Carteira de Trabalho"]=carteira_detrabalho

#CASO TENHA CARTEIRA DE TRABALHO
if carteira_detrabalho==1:
    dados_pessoa["Ano de contratação"]=verifica.verifica_int(input("Ano de contratação: "))
    dados_pessoa["Salário"]=verifica.verifica_float(input("Salário: "))
    print()#2
    #DEFININDO CONDIÇÕES PARA APOSENTADORIA
    #CASO SEJA MULHER - 60 ANOS OU 30 DE CONTRIBUIÇÃO
    if dados_pessoa["Sexo"] in ["F","MULHER","FEMININO"]:
        print("Condições para aposentadoria da mulher:\n"
              "Idade mínima: 60 anos\n"
              "Tempo mínimo de contribuição: 30 anos\n")
        tempoPara_aposentar=60-idade
        tempoContribuicao=ano_atual-dados_pessoa["Ano de contratação"]
        if tempoPara_aposentar<=0 or tempoContribuicao>=30:
            print("Já pode se aposentar! Você tem: \n"
                  f"Idade: {idade}\n"
                  f"Tempo de contribuição: {tempoContribuicao}")
        elif tempoPara_aposentar>0 and tempoContribuicao<30:
            print("Você ainda não pode se aposentar!\n"
                  f"Idade: {idade}\n"
                  f"Tempo de contribuição: {tempoContribuicao}")
        dados_pessoa["Idade mínima para aposentar"]=idade+tempoPara_aposentar

    #CASO SEJA HOMEM - 65 ANOS OU 35 DE CONTRIBUIÇÃO
    elif dados_pessoa["Sexo"] in ["M","MASCULINO","HOMEM"]:
        print("Condições para aposentadoria do homem:\n"
              "Idade mínima: 65 anos\n"
              "Tempo mínimo de contribuição: 35 anos\n")
        print()
        tempoPara_aposentar=65-idade
        tempoContribuicao=ano_atual-dados_pessoa["Ano de contratação"]
        #CASO POSSA SE APOSENTAR POR UMA DAS CONDIÇÕES
        if tempoPara_aposentar<=0 or tempoContribuicao>=35:
            print("Já pode se aposentar! Você tem: \n"
                  f"Idade: {idade}\n"
                  f"Tempo de contribuição: {tempoContribuicao}")
        #CASO NÃO POSSA SE APOSENTAR POR
        elif tempoPara_aposentar>0 and tempoContribuicao<35:
            print("Você ainda não pode se aposentar!\n"
                  f"Idade: {idade}\n"
                  f"Tempo de contribuição: {tempoContribuicao}")
        dados_pessoa["Idade mínima para aposentar"] = idade + tempoPara_aposentar

print(dados_pessoa)
print()


#---------------------------------------------------------
print("DESAFIO - APROVEITAMENTO JOGADOR")
jogador=dict()
gols=list()
total_gols=0

#ENTRADA DE NOME E NÚMERO DE PARTIDAS
jogador["Nome"]=str(input("Nome do jogador: "))
n_partidas=verifica.verifica_int(input(f"Quantas partidas {jogador["Nome"]} jogou? "))

#INFORMAÇÃO DE NÚMERO DE GOLS DE CADA PARTIDA SALVA NUMA LISTA, QUE É ADICIONADA AO DICIONÁRIO
for cont in range(0,n_partidas):
    n_gols=verifica.verifica_int(input(f"Quantos gols na partida {cont+1}: "))
    gols.append(n_gols)
jogador["Gols"]=gols[:]

#PARA CADA NÚMERO DE GOLS INFORMADO, SOMO TUDO NUMA VARIÁVEL E ADICIONO ESSA VARIÁVEL NO DICIONÁRIO
for gol in gols:
    total_gols+=gol
jogador["Total de gols"]=total_gols

#MOSTRANDO RESULTADO NA TELA
print(f"{jogador["Nome"]} jogou {n_partidas} partidas!")
for pos,valor in enumerate(jogador["Gols"]):
    print(f"Na partida {pos+1}, fez {valor} gols.")
print(f"{jogador["Nome"]} fez um total de {jogador["Total de gols"]} gols!")
print()


#---------------------------------------------------------
print("DESAFIO - DADOS DE VÁRIAS PESSOAS")
pessoas=list()
mulheres=list()
idades_acima_media=list()
pessoa=dict()
continuar=True
soma_idades=media_idade=0

while continuar:
    #ENTRADA DE DADOS PELO USUÁRIO - NOME, SEXO E IDADE
    pessoa["Nome"]=str(input("Nome da pessoa: "))
    sexo = str(input("Sexo: "))
    sexo = sexo.upper()
    while sexo not in ["F", "MULHER", "FEMININO", "M", "HOMEM", "MASCULINO"]:
        print("Entrada inválida! Tente novamente.")
        sexo = str(input("Sexo: "))
        sexo=sexo.upper()
    pessoa["Sexo"]=sexo
    pessoa["Idade"]=verifica.verifica_int(input("Idade: "))

    #ATRIBUIÇÃO DO DICIONÁRIO À LISTA
    pessoas.append(pessoa.copy())

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False

print(pessoas)

#NÚMERO DE PESSOAS CADASTRADAS
n_pessoas=len(pessoas)

#MÉDIA DE IDADE DO GRUPO
for pessoa in pessoas:
    soma_idades+=pessoa["Idade"]
media_idade=verifica.verifica_int(soma_idades/n_pessoas)

#LISTA COM TODAS AS MULHERES
for pos,pessoa in enumerate(pessoas):#PARA CADA ITEM DA LISTA PESSOAS, OU SEJA, CADA DICIONÁRIO
    if pessoa["Sexo"] in ["F", "MULHER", "FEMININO"]:#SE NO CAMPO SEXO FOR MULHER
        mulheres.append(pessoas[pos].copy())#COPIO ESSE DICIONÁRIO PARA A LISTA MULHERES

#LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
for pos,pessoa in enumerate(pessoas):
    if pessoa["Idade"]>media_idade:#SE ESSA PESSOA TIVER A IDADE ACIMA DA MÉDIA
        idades_acima_media.append(pessoas[pos].copy())#ADICIONO ELA À LISTA idades.....

#MOSTRANDO RESULTADOS NA TELA
for pos,pessoa in enumerate(pessoas):
    print(f"{pos+1}º pesssoa\n"
          f"Nome: {pessoa["Nome"]}\n"
          f"Sexo: {pessoa["Sexo"]}\n"
          f"Idade: {pessoa["Idade"]}\n")#USO DE FSTRING

print(f"Quantas pessoas foram cadastradas: {n_pessoas}\n"
      f"Média de idade do grupo: {media_idade}")

print("Mulheres do grupo: ")
for mulher in mulheres:
    print(mulher["Nome"],end=" - ")
print()
print()

print("Pessoas com idade acima da média:")
for p in idades_acima_media:
    print(f"{p["Nome"]}...Idade: {p["Idade"]}")#USO DE FSTRING
print()


#---------------------------------------------------------
print("DESAFIO - APROVEITAMENTO JOGADORES")
jogadores=list()
jogador=dict()
gols=list()
total_gols=0
continuar=True


while continuar==True:
    #ENTRADA DE NOME E NÚMERO DE PARTIDAS
    jogador["Nome"]=str(input("Nome do jogador: "))
    n_partidas=verifica.verifica_int(input(f"Quantas partidas {jogador["Nome"]} jogou? "))

    #INFORMAÇÃO DE NÚMERO DE GOLS DE CADA PARTIDA SALVA NUMA LISTA, QUE É ADICIONADA AO DICIONÁRIO
    total_gols = 0
    for cont in range(0,n_partidas):
        n_gols=verifica.verifica_int(input(f"Quantos gols na partida {cont+1}: "))
        gols.append(n_gols)
    jogador["Gols"]=gols[:]

    #PARA CADA NÚMERO DE GOLS INFORMADO, SOMO TUDO NUMA VARIÁVEL E ADICIONO ESSA VARIÁVEL NO DICIONÁRIO
    for gol in gols:
        total_gols+=gol
    jogador["Total"]=total_gols
    gols.clear()#LIMPANDO A LISTA GOLS PARA USAR NA PRÓXIMA ITERAÇÃO

    #ADICIONANDO O JOGADOR À LISTA
    jogadores.append(jogador.copy())

    #MOSTRANDO RESULTADO NA TELA

    print(f"{jogador["Nome"]} jogou {n_partidas} partidas!")
    for pos,valor in enumerate(jogador["Gols"]):
        print(f"Na partida {pos+1}, fez {valor} gols.")
    print(f"{jogador["Nome"]} fez um total de {jogador["Total"]} gols!")

    # OPÇÃO AO USUÁRIO DE CONTINUAR OU NÃO
    op = input("Deseja continuar? [S/N]")
    op = op.upper()
    while op not in ["S", "N", "SIM", "NÃO", "NAO"]:
        print("Entrada inválida. Tente novamente!")
        op = input("Deseja continuar? [S/N]")
        op = op.upper()
    if op in ["N", "NAO", "NÃO"]:
        continuar = False

print(jogadores)
#MOSTRANDO INFORMAÇÕES NA TELA
#CABEÇALHO
print("cod ",end="")
for chave in jogador.keys():
    print(f"{chave:<15}",end="")
print()

#TABELA
for pos,valores in enumerate(jogadores):
    print(f"{pos:<4}",end="")
    for valor in valores.values():
        print(f"{str(valor):<15}",end="")
    print()

while True:#LAÇO INFINITO
    escolha=verifica.verifica_int(input("Mostrar dados de qual jogador: (999 - SAIR)\n -->"))

    if escolha>=len(jogadores):#CASO A ESCOLHA SEJA UM COD ACIMA DA LISTA CADASTRADA, ERRO
        print("Erro! Jogador não cadastrado")
    else:
        print(f"Levantamento do jogador {jogadores[escolha]["Nome"]}")
        # ACESSANDO A LISTA DE GOLS DO DICIONÁRIOS
        for pos,valor in enumerate(jogadores[escolha]["Gols"]):
            print(f"Na {pos+1}º partida, fez {valor} gols!")
        print()

    if escolha==999:#CONDIÇÃO DE SAÍDA
        break
print()