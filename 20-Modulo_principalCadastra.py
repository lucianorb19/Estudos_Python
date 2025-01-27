from Pacote1 import moduloCadastra

while True:#ENQUANTO NÃO CHEGAR NO BREAK
    try:
        print("-" * 30)
        print(f"{"MENU PRINCIPAL":^30}")
        print("-" * 30)
        print("1 - Listar base de dados\n"
              "2 - Cadastrar nova pessoas\n"
              "3 - Sair do sistema")
        op=int(input("--> "))
        while op not in [1,2,3]:
            op=int(input("Opção inválida. Tente novamente!\n--> "))

    except KeyboardInterrupt:#CASO O USUÁRIO SELECIONE ALGUMA OPÇÃO PARA TERMINAR NA INTERFACE
        print("Terminado pelo usuário!")
        break
    except:#NOS DEMAIS CASOS DE EXCEÇÃO
        print("Opção inválida! Tente novamente.")
    else:#CASO SEJA UMA ENTRADA VÁLIDA
        if op==1:
            moduloCadastra.listar_pessoas()
        elif op==2:
            print("FUNÇÃO CADASTRAR")
            moduloCadastra.cadastrar_pessoa()
        elif op==3:
            print("Até logo!")
            break


#import os

#caminho=os.path.dirname(os.path.realpath(__file__))
#print(f"Caminho atual: {caminho}")
