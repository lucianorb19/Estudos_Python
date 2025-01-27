def listar_pessoas():
    #CABEÇALHO
    print("-"*30)
    print(f"{"PESSOAS CADASTRADAS":^30}")
    print("-" * 30)

    import os
    #especifico o caminho do arquivo para usar com a função open
    caminho=os.path.dirname(os.path.realpath(__file__))
    
    #LEITURA DO ARQUIVO Pessoas POR LINHA
    try:
        with open(caminho+"Pessoas.txt","r") as arquivo:
            linha=arquivo.readline()
            if linha=="":
                print("Arquivo vazio!")
            while linha !="":
                print(linha)
                linha=arquivo.readline()#VAI PARA A PRÓXIMA LINHA
            #arquivo.close() SÓ É NECESSÁRIO CASO O WITH NÃO SEJA USADO
    except IOError:#CASO O ARQUIVO NÃO EXISTA
        #print(f"Caminho atual: {caminho}")
        arquivo=open(caminho+"Pessoas.txt","x") #CRIO O ARQUIVO
        print("Arquivo "+caminho+".txt criado neste momento! Ele não existia anteriormente.")
    except Exception as erro:
        print(f"Não foi possível ler o arquivo Pessoas.txt!\n-->{erro}")


def cadastrar_pessoa():
    #CABEÇALHO
    print("-" * 30)
    print(f"{"CADASTRAR PESSOA":^30}")
    print("-" * 30)

    import os
    #especifico o caminho do arquivo pra usar na função open
    caminho=os.path.dirname(os.path.realpath(__file__))
    
    while True:#ENQUANTO NÃO CHEGAR NO BREAK
        try:#TRATAMENTO DA ENTRADA DO USUÁRIO
            nome=input("Nome: ")
            idade=int(input("Idade: "))
        except KeyboardInterrupt:
            print("Dado não informado pelo usuário! Operação cancelada")
            break
        except Exception as erro:
            print(f"Erro na entrada do usuário!\n->>{erro}\nTente novamente.")
        else:#CASO SEJAM INSERIDAS ENTRADAS VÁLIDAS
            try:#TRATAMENTO DA MANIPULAÇÃO DO ARQUIVO
                # ESCRITA DA ENTRADA DO USUÁRIO AO FINAL DO ARQUIVO, NUMA NOVA LINHA
                with open(caminho+"Pessoas.txt", "a") as arquivo:
                    arquivo.write(f"\n{nome},{idade}")
            except Exception as erro:
                print(f"Erro na manipulação do arquivo!\n{erro}Operação cancelada.")
            else:#CASO A PESSOA SEJA CADASTRADA
                print(f"{nome} de {idade} anos cadastrado(a)!")
                break


