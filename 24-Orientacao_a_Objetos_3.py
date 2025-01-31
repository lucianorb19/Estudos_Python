"""
POLIMORFISMO DE CLASSES
POLIMORFISMO É UMA CARACTERÍSTICA DA ORIENTAÇÃO A OBJETOS QUE PERMITE QUE CLASSES HERDEM ATRIBUTOS COM O MESMO NOME, MAS COM VALORES/FUNCIONAMENTOS DIFERENTES, ISSO PERMITE QUE PROPRIEDADES/FUNÇÕES DE MESMO NOME TENHAM VALORES/COMPORTAMENTOS ESPECÍFICOS A DEPENDER DA CLASSE A QUAL PERTENCEM. POR EXEMPLO, UMA CLASSE Animal QUE TEM A FUNÇÃO emitir_som, E UMA CLASSE Cachorro, QUE HERDA OS ATRIBUTOS DE Animal, MAS MODIFICA SEU COMPORTAMENTO/VALOR

class Animal:
    def emitir_som(self):
        print("Um som qualquer!")

class Cachorro(Animal):
    def emitir_som(self):
        print("Latindo...")

DA MESMA FORMA, PODE HAVER UMA OUTRA CLASSE Gato, QUE HERDA OS ATRIBUTOS DE Animal E MUDA SEU COMPORTAMENTO/VALOR

class Gato(Animal):
    def emitir_som(self):
        print("Miando...")

"""

class Animal:
    peso="100kg"
    def emitir_som(self):
        print("Um som qualquer!")

class Cachorro(Animal):
    peso="30kg"
    def emitir_som(self):
        print("Latindo...")
        
class Gato(Animal):
    peso="3kg"
    def emitir_som(self):
        print("Miando...")
        
meu_cachorro=Cachorro()
meu_cachorro.emitir_som()
print(meu_cachorro.peso)
print()

meu_gato=Gato()
meu_gato.emitir_som()
print(meu_gato.peso)