"""
HERANÇA

HERANÇA É UM PARADIGMA DA ORIENTAÇÃO A OBJETOS. ELA PERMITE QUE CLASSES COM ATRIBUTOS GENÉRICOS TENHAM SUAS CARACTERÍSTICAS PASSADAS PARA OUTRAS CLASSES, SEM A NECESSIDADE DE DUPLICAR O CÓDIGO. ISSO GERA PRATICIDADE AO CÓDIGO E PERMITE ABSTRAIR COM MAIS FACILIDADE A REALIDADE. POR EXEMPLO, UMA CLASSE GENÉRICA Carro, QUE TEM AS CARACTERÍSTICAS QUE TODO CARRO TEM 

class Carro:
    numero_rodas=4
    assentos=5

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando")

E A PARTIR DELA, CRIA-SE A CLASSE Uno, QUE HERDA SEUS ATRIBUTOS E ADICIONA NOVOS ESPECÍFICOS DE UM CARRO UNO

class Uno(Carro):#AQUI SE DEFINE QUE A CLASSE Uno É HERDEIRA/FILHA DA CLASSE Carro
    modelo="Uno"
    marca="Fiat"
    ano="2005"

"""

class Carro:
    numero_rodas=4
    assentos=5

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando")

class Uno(Carro):#AQUI SE DEFINE QUE A CLASSE Uno É HERDEIRA/FILHA DA CLASSE Carro
    modelo="Uno"
    marca="Fiat"
    ano="2005"



meu_carro=Uno()
meu_carro.acelerar()
print(meu_carro.numero_rodas)
print(meu_carro.modelo)