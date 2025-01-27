from Pacote1.moduloDado import principalDado
from Pacote1.moduloMoeda import teste1

preco=input("Digite o valor: ")
preco=principalDado.leiaDinheiro(preco)
teste1.resumo(preco)


#não funciona se receber valores que misturam letras e números