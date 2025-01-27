def metade(numero=0,op=True):
    metade = numero / 2
    if op:
        return f"R${metade:.2f}".replace(".", ",")
    else:
        return metade


def dobro(numero=0,op=True):
    dobro=numero*2
    if op:
        return f"R${dobro:.2f}".replace(".", ",")
    else:
        return dobro


def aumenta10(numero=0,op=True):
    aumentado=numero+(numero/10) #AUMENTA O VALOR EM 10%
    if op:
        return f"R${aumentado:.2f}".replace(".", ",")
    else:
        return aumentado


def diminui20(numero=0,op=True):
    diminuido=numero-(numero/5) #DIMINUI O VALOR EM 20%
    if op:
        return f"R${diminuido:.2f}".replace(".", ",")
    else:
        return diminuido

def resumo(numero):
    print(f"X"*30)
    print(f"{"Resumo da Análise":^30}") #AO CENTRO EM 30 ESPAÇOS
    print(f"Valor avaliado: {numero}")
    print(f"Metade: {metade(numero,True)}\n"
          f"Dobro: {dobro(numero,True)}\n"
          f"Aumentado 10%: {aumenta10(numero,True)}\n"
          f"Diminuído 20%: {diminui20(numero,True)}")
