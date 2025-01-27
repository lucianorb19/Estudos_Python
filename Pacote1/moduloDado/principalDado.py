def leiaDinheiro(valor):
    valido=False
    valor=str(valor)#CONVERTENDO EM STR PARA FAZER AS VERIFICAÇÕES
    valor=valor.replace(",",".")#SUBSTITUINDO , POR .
    while not valido:#ENQUANTO VÁLIDO FOR FALSO
        if valor.isalpha() or valor.strip()=="":#SE TIVER SOMENTE LETRAS OU
                                                #SE FICAR VAZIO AO TIRAR OS ESPAÇOS ANTES E DPOIS
            valor=str(input("Entrada inválida. Tente novamente!\n--> ")).replace(",",'.')
        else:
            valido=True

    return float(valor)
