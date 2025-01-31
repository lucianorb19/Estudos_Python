"""
POLIMORFISMO DE INTERFACE

É UMA CARACTERÍSTICA DA ORIENTAÇÃO A OBJETOS QUE PERMITE CRIAR, ASSIM COMO NO POLIMORFISMO DE CLASSES, ATRIBUTOS COM OS MESMOS NOMES, MAS COM COMPORTAMENTOS DIFERENTES. NO CASO DO POLIMORFISMO DE INTERFACE, A DIFERENÇA ESTÁ NO FATO DE QUE NA CLASSE BASE, QUE SERÁ HERDADA PELAS CLASSES SEGUINTES, A FUNCÃO NÃO FAZ NADA E O SEU COMPORTAMENTO SÓ É ESPECIFICADO NA CLASSE FILHA, COM O USO TAMBÉM DE UM CONSTRUTOR. NO EXEMPLO ABAIXO, UMA CLASSE Forma, COM UMA FUNÇÃO area QUE NÃO FAZ NADA

class Forma:
    def area():
        pass
        
E NA CLASSE Quadrado, QUE É FILHA DE Forma, TEM-SE DUAS COISAS, O CONSTRUTOR DA CLASSE, QUE É A ESTRUTURA QUE DEFINE COMO O OBJETO DEVE SER MONTADO TODA VEZ QUE FOR INSTANCIADO. NO CASO EM QUESTÃO, É DEFINIDO QUE EM TODA INSTANCIAÇÃO DO Quadrado, DEVE SER PASSADO UM PARÂMETRO lado QUE VAI SER ATRIBUÍDO À VARIÁVEL self.lado, DA ESTRUTURA DA CLASSE.

class Quadrado(Forma):

    def __init__(self,lado):
        self.lado=lado


COMO ESSA VARIÁVEL self.lado É DEFINIDA SEMPRE QUE UM OBJETO Quadrado É INSTANCIADO, OUTRAS FUNÇÕES DA CLASSE QUADRADO PODEM UTILIZÁ-LA, OU SEJA, NO PROGRAMA PRINCIPAL NÃO PRECISO DEFINI-LA. NESSE CASO, A FUNÇÃO area DA CLASSE QUADRADO, QUE É UMA HERANÇA POLIMÓRFICA DA CLASSE Forma, UTILIZA ESSA VARIÁVEL NO SEU FUNCIONAMENTO.

    def area(self,lado):#FUNÇÃO QUE USA O VALOR PASSADO NO CONSTRUTOR PARA EXECUTAR SEU COMPORTAMENTO
            return self.lado**2

AGORA UMA OUTRA CLASSE Circulo QUE UTILIZA O MESMO CONCEITO DA CLASSE Quadrado MAS MUDANDO O COMPORTAMENTO DA FUNCAO area

class Circulo(Forma):

    def __init__(self,raio):
        self.raio=raio

    def area(self):
        return 3.14*(self.raio**2)


"""

class Forma:
    def area():#FUNÇÃO BASE, NÃO FAZ NADA
        pass

class Quadrado(Forma):#CLASSE Quadrado FILHA DE Forma

    def __init__(self,lado):#CONSTRUTOR DA CLASSE
        self.lado=lado
    
    def area(self):#FUNÇÃO QUE USA O VALOR PASSADO NO CONSTRUTOR PARA EXECUTAR SEU COMPORTAMENTO
        return self.lado**2
    
class Circulo(Forma):

    def __init__(self,raio):
        self.raio=raio

    def area(self):
        return 3.14*(self.raio**2)
        
    

meu_quadrado=Quadrado(3)
area_quadrado=meu_quadrado.area()
print(f"Área do quadrado: {area_quadrado}")

meu_circulo=Circulo(2)
area_circulo=meu_circulo.area()
print(f"Área do círculo: {area_circulo}")