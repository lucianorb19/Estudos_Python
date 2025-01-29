def verifica_int(numero):
    """
    FUNÇÃO
    """
    while True:#ENQUANTO NÃO CHEGAR NO BREAK
        numero=numero.strip()#RETIRAR ESPAÇOS ANTES E DEPOIS
        try:#TENTA CONVERTER PARA INTEIRO
            numero=int(numero)
        except:#SE NÃO CONSEGUIR, RECEBE OUTRA ENTRADA
            numero=input("Número não é inteiro. Tente novamente.\n--> ")
        else:#CASO A CONVERSÃO SEJA POSSÍVEL
            return numero
            break#FIM DO LAÇO

def verifica_float(numero):
    while True:#ENQUANTO NÃO CHEGAR NO BREAK
        numero=numero.strip()#RETIRAR ESPAÇOS ANTES E DEPOIS
        numero=numero.replace(",",".")#SUBSTITUI AS VÍRGULAS(,) POR PONTO(.)
        try:#TENTA CONVERTER PARA FLOAT
            numero=float(numero)
        except:#SE NÃO CONSEGUIR, RECEBE OUTRA ENTRADA
            numero=input("Número não é float. Tente novamente.\n--> ")
        else:#CASO A CONVERSÃO SEJA POSSÍVEL
            return numero
            break#FIM DO LAÇO


        

a=verifica_float(input("Digite um número real: "))
print(a)