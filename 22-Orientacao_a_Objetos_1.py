"""
ORIENTAÇÃO A OBJETOS

A Orientação a Objetos permite criar classes com atributos (propriedades e funções), e instâncias dessas classes, que são variáveis que têm todas os atributos definidos na classe. Por exemplo, uma classe Celular, que traz diversas propriedades (características do celular) e funções (funcionalidades do celular)

#ESTRUTURA DA CLASSE
class Celular:
    #PROPRIEDADES
    marca = "Nokia"
    cor = "Azul"
    tem_camera = False
    bateria = "quase_infinita"

    #FUNÇÕES
    def fazer_ligacao(self):
        print("Fazendo ligação...")
    
    def jogar_cobrinha(self):
        print("Jogando cobrinha...")
    #self É O PRIMEIRO PARÂMETRO OBRIGATÓRIO DE TODA FUNÇÃO DE UMA CLASSE
    #ELE INDICA A FUNÇÃO À CLASSE

    def soma(self,valor_1,valor_2):
        return valor_1+valor2

#INSTANCIAÇÃO DO OBJETO meu_celular, DA CLASSE Celular
meu_celular = Celular()

#UTILIZANDO UM DE SEUS ATRIBUTOS
print(meu_celular.bateria)

#UTILIZANDO UMA DE SUAS FUNÇÕES
meu_celular.fazer_ligacao()


"""
#ESTRUTURA DA CLASSE
class Celular:
    #PROPRIEDADES
    marca = "Nokia"
    cor = "Azul"
    tem_camera = False
    bateria = "quase_infinita"

    #FUNÇÕES
    def fazer_ligacao(self):
        print("Fazendo ligação...")
    
    def jogar_cobrinha(self):
        print("Jogando cobrinha...")
    #self É O PRIMEIRO PARÂMETRO OBRIGATÓRIO DE TODA FUNÇÃO DE UMA CLASSE
    #ELE INDICA A FUNÇÃO À CLASSE

    def soma(self,valor_1,valor_2):
        return valor_1+valor_2

#INSTANCIAÇÃO DO OBJETO meu_celular, DA CLASSE Celular
meu_celular = Celular()

#UTILIZANDO UM DE SEUS ATRIBUTOS
print(meu_celular.bateria)

#UTILIZANDO UMA DE SUAS FUNÇÕES
meu_celular.fazer_ligacao()

#UTILIZANDO UMA DE SUAS FUNÇÕES QUE TEM RETORNO
resultado=meu_celular.soma(2,3)
print(resultado)