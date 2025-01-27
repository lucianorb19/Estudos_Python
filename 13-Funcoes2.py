"""
INTERACTIVE HELP
DIGITAR help() NO CONSOLE PYTHON
OU
NO CÓDIGO, DIGITAR help(comando)
OU
print(comando.__doc__)

DOCSTRING
CRIAR A DOCUMENTAÇÃO PARA UMA FUNÇÃO. ISSO É FEITO COLOCANDO COMENTÁRIO COM ASPAS
DUPLAS LOGO ABAIXO DO CABEÇALO DA FUNÇÃO

PARÂMETROS OPCIONAIS
EXPLICITAR NA DEFINIÇÃO DA FUNÇÃ QUE O PARÂMETRO RECEBE UM VALO X QUANDO NA SUA CHAMADA
NÃO FOR PASSADO VALOR
def soma(a,b,c=0):
    soma=a+b+c
    print(soma)

E NO CÓDIGO PRINCIPAL
soma(2,4,6)
soma(2,1)

A SEGUNDA CHAMADA TAMBÉM FUNCIONA, PORQUE CASO NÃO SEJA PASSADO O VALOR DO PARÂMETRO OPCIONAL c,
ELE ASSUME VALOR 0

ESCOPO DE VARIÁVEIS
A VARIÁVEL DECLARADA NO PROGRAMA PRINCIPAL TEM ESCOPO GLOBAL, OU SEJA, ELA É VISÍVEL
TAMBÉM DENTRO DAS FUNÇÕS
A VARIÁVEL DECLARADA DENTRO DA FUNÇÃO TEM ESCOPO LOCAL, OU SEJA, SÓ É VISÍVEL DENTRO
DA FUNÇÃO
DEFINIÇÃO DE UMA VARIÁVEL DE MESMO NOME NO PROGRAMA PRINCIPAL E TAMBÉM NA FUNÇÃO CRIA
DUAS VARIÁVEIS DE MESMO NOME, UMA GLOBAL E UMA LOCAL
def mostra()
a=2
print(f"a local vale {a}") #2

No código principal
a=5
print(f"a global vale {a}") #5

NA FUNÇÃO, PARA ESPECIFICAR QUE DEVE SER PROCESSADA A VARIÁVEL GLOBAL, É PRECISO 
USAR global nome_variavel NA SUA DECLARAÇÃO DA FUNÇÃO
def mostra()
    global a


RETORNO DE FUNÇÃO
USAR return AO FINAL DELA
def soma(a=0,b=0,c=0):
    s=a+b+c
    return s

NO CÓDIGO PRINCIPAL
total=soma(4,9,2)
print(total)
"""


from datetime import datetime
def voto(ano_nascimento1):
    ano_atual = datetime.now().year
    idade=ano_atual-ano_nascimento1
    print(f"Você completa {idade} anos em {ano_atual}!")
    #VOTO NEGADO
    if idade<16:
        return "Voto negado!"
    #VOTO OPCIONAL
    elif idade==16 or idade==17 or idade>=70:
        return "Voto opcional!"
    #VOTO OBRIGATÓRIO
    elif idade>=18 and idade <70:
        return "Voto obrigatório!"


def fatorial(numero1,show1=False):
    total_fatorial=numero1
    if show1:
        for valor in range(numero1-1,0,-1):
            print(f"{total_fatorial} x {valor} = ",end="")
            total_fatorial*=valor
            print(f"{total_fatorial}")
    else:
        for valor in range(numero1-1,0,-1):
            #print(f"{total_fatorial} x {valor} = ",end="")
            total_fatorial*=valor
            #print(f"{total_fatorial}")
    print(f"Fatorial de {numero1} é {total_fatorial}!")


def mostra_dados(nome1="<Desconhecido>",gols1=0):
    print(f"O jogador {nome1} marcou {gols1} gols no campeonato!")


def leia_int(mensagem):
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            numero=int(numero)
            break
        else:
            print("Entrada inválida. Tente novamente!")
    return numero


def notas(*notas,status1=False):
    """
    *notas-> Recebe vários valores numéricos, cada um representando
    uma nota do aluno
    status1 -> variável boleana opcional. Se for True, o status do aluno
    é mostrado na tela e adicionado ao dicionário
    """
    alunos=dict()
    n_notas=maior=soma_notas=media_notas=0
    menor=1000

    #CALCULO QUANTIDADE DE NOTAS
    n_notas=len(notas)
    alunos["Quatidade de Notas"]=n_notas
    #CALCULO MAIOR, MENOR E MEDIA NOTAS
    for x in notas:
        if x>=maior:
            maior=x
        if x<=menor:
            menor=x
        soma_notas+=x
    media_notas=soma_notas/n_notas
    alunos["Maior nota"]=maior
    alunos["Menor nota"]=menor
    alunos["Nota média"]=media_notas
    if status1:
        if alunos["Nota média"]<6:
            alunos["Status"]="Reprovado"
        if alunos["Nota média"]>=6:
            alunos["Status"]="Aprovado"

    return alunos


def pyHelp():
    #CEBEÇALHO
    print("~" * 30)
    msg = "SISTEMA DE AJUDA PYHELP"
    print(f"{msg:^30}")
    print("~" * 30)

    #SE A ENTRADA FOR FIM, SÓ RETORNO O VALOR PARA O PROGRAMA PRINCIPAL
    pesquisar1=str(input("Função ou Biblioteca: [FIM - SAIR]\n--> "))
    if pesquisar1 in ["FIM","fim"]:
        return pesquisar1
    #SE NÃO, EFETUO O HELP E DPOIS RETORNO PARA O PROGRAMA PRINCIPAL
    else:
        resultado1=help(pesquisar1)
        return pesquisar1


#CÓDIGO PRINCIPAL
#------------------------------------------------------
print("DESAFIO - VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO")
#negado <16
#opcional 16,17,>=70
#obrigatório >=18 e <=69

ano_nascimento=int(input("Qual seu ano de nascimento? "))
status=voto(ano_nascimento)
print(status)
print()


#------------------------------------------------------
print("DESAFIO - FATORIAL")
show=False
#ENTRADA DO USUÁRIO
numero=int(input("Número para cálculo do fatorial: "))

#OPÇÃO DE MOSTRAR O CÁLCULO OU NÃO
op=str(input("Mostrar cálculo na tela [S/N]?"))
op=op.upper()
while op not in ["SIM","S","N","NAO","NÃO"]:
    op=str(input("Opção inválida. Tente novamente!\n->> "))
    op=op.upper()

#CASO O USUÁRIO ESCOLHA MOSTRAR, CHAMO A FUNÇÃO DEFININDO TODOS PARÂMETROS
if op in ["SIM","S"]:
    show=True
    fatorial(numero,show)
#CASO NÃO, A FUNÇÃO TEM O SEGUNDO PARÂMETRO OPCIONAL QUE JÁ RECEBE VALOR FALSE AUTOMATICO
else:
    fatorial(numero)
print()


#------------------------------------------------------
print("DESAFIO - DADOS DO JOGADOR")
nome=str(input("Nome do jogador: "))
#VALOR DE GOLS É str PQ O PYTHON NÃO DEIXA RECEBER ENTRADA DE int VAZIA
gols=str(input("Nº de gols marcados: "))
if gols.isnumeric():#SE O VALOR DIGITADO PUDER SER CONVERTIDO PRA NUMÉRICO
    gols=int(gols)
else:#caso seja qualquer entrada não numérica, gols vira 0
    while True:
        gols=str(input("Número de gols não é um número inteiro."
                       "Digite novamente!\n-->"))
        if gols.isnumeric():  # SE O VALOR DIGITADO PUDER SER CONVERTIDO PRA NUMÉRICO
            gols = int(gols)
            break

if nome.strip()=="":#CASO O NOME, APÓS RETIRAR OS ESPAÇOS VAZIOS ANTES E DPOIS, SEJA VAZIO
    mostra_dados(gols1=gols)                #OU SEJA, NADA FOI DIGITADO ALÉM DE ESPAÇOS
    #DEFINIÇÃO DO PARÂMETRO gols1, DA FUNÇÃO, COMO gols, DO PROGRAMA PRINCIPAL
print()


#------------------------------------------------------
print("DESAFIO - FUNÇÃO QUE SÓ ACEITA NÚMERO INTEIRO")

n=leia_int("Digite um número inteiro: ")
print(f"O número inteiro digitado foi {n}")
print()


#------------------------------------------------------
print("DESAFIO - DICIONÁRIO COM INFORMAÇÕES DE NOTAS")
alunos1=dict()

help(notas)
#OPÇÃO DE MOSTRAR O CÁLCULO OU NÃO
op=str(input("Mostrar situação dos aluno [S/N]? "))
op=op.upper()
while op not in ["SIM","S","N","NAO","NÃO"]:
    op=str(input("Opção inválida. Tente novamente!\n->> "))
    op=op.upper()

#CASO O USUÁRIO ESCOLHA MOSTRAR, CHAMO A FUNÇÃO DEFININDO TODOS PARÂMETROS
if op in ["SIM","S"]:
    status=True
    alunos1=notas(2, 4, 5,10,10, status1=status)
#CASO NÃO, A FUNÇÃO TEM O SEGUNDO PARÂMETRO OPCIONAL QUE JÁ RECEBE VALOR FALSE AUTOMATICO
else:
    alunos1=notas(2,4,5,10,10)

for chave, valor in alunos1.items():
    print(f"{chave}:{valor}")
print()


#------------------------------------------------------
print("DESAFIO - UTILIZAR O INTERACTIVE HELP")

while True:
    pesquisar=pyHelp()
    if pesquisar in ["FIM","fim"]:
        break
print()