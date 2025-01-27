"""
try:
    .....
except:
    .....
else:
    ....
finally:
    .....

O try TENTA EXECUTAR OQ TIVER NO CÓDIGO, SE CONSEGUIR, VAI PARA O else,SE NÃO CONSEGUIR,
CAI NO excepet.O finally SEMPRE É EXECUTADO.

NO except, PODEMOS DEFINIR UM except PARA CADA TIPO DE ERRO
try
    .....
except NameError:
    .....
except ValueError:
    .....
except (ZeroDivisionError, TypeError):
    .....

Por exemplo, definir um código específico para o tipo de erro divisão por zero
try
    a=10/0
except ZeroDivisionError:
    print("Não pode haver divisão por zero!")
else:
    print(a)
finally:
    print("Volte sempre!")


NO except, PODEMOS UTILIZAR O CÓDIGO DO ERRO, com o Exception
try
    ......
except Exception as erro:
    print(f"O erro foi {erro.__cause__}")

NO CASO ACIMA, É MOSTRADO A CAUSA DO ERRO. TAMBÉM PODERIA SER UTILIZADO A CLASSE(__class__),
DENTRE OUTRAS


PODEM SER DEFINIDOS VARIOS except PELO TIPO DE ERRO
NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
EOFError
KeyboardInterrupt
OSErrror
MemoryError
ConnectionError
RunTimeError
"""
import urllib
import urllib.request


def leia_int():
    while True:#ENQUANTO NÃO CHEGAR NO return OU break
        try:
            numero=input("Digite um número inteiro: ")
            numero=str(numero).strip() #tratando espaços antes e dpois
            numero=int(numero)
        except Exception as erro:
            print(f"Entrada inválida: {erro}. Tente novamente!")
        except KeyboardInterrupt:
            print("Nenhuma entrada para valor inteiro!")
            numero=0
            return numero
        else:
            print("Deu certo!")
            return numero #USO DO RETURN FECHA O LOOP


def leia_float():
    while True:#ENQUANTO NÃO CHEGAR NO RETURN OU BREAK
        try:
            numero=input("Digite um número real: ")
            numero=str(numero).strip()#convertendo e tirando espaços antes e dpois
            numero=numero.replace(",",".") #substituindo , por .
            numero=float(numero)#convertendo o resultado para float
        except Exception as erro:
            print(f"Entrada inválida: {erro}\nTente novamente!")
        except KeyboardInterrupt:
            print("Nenhuma entrada para valor real!")
            numero=0
            return numero
        else:
            print("Deu certo!")
            return numero #USO DO RETURN FECHA O LOOP


def acessaSite():
    try:
        url=str(input("Digite o endereço do site: "))
        url=url.strip()#TRATANDO ESPAÇOS ANTES E DEPOIS
        acesso=urllib.request.urlopen(url)
    #UM DESES DOIS ERROS FUNCIONA
    except urllib.error.URLError:
        print("Site não acessível no momento! 2")
    except urllib.request.URLError:
        print("Site não acessível no momento! 1")
    else:
        print("Site Acessível")




#PROGRAMA PRINCIPAL
"""
print("DESAFIO - FUNÇÃO QUE LEIA SOMENTE INT OU FLOAT")
numero1=leia_int()
numero2=leia_float()
print(f"Número inteiro: {numero1}\n"
      f"Número real: {numero2}")
"""
print("DESAFIO - TENTIVA DE ACESSAR SITE")
acessaSite() #NÃO FUNCIONA POR CAUSA DO PROXY. VOU CONSERTAR? NÃO




