class Chinela:
    def __init__(self)
        self.__tamanho: int = 0
    def getTamanho (self):
        return self.__tamanho
    def setTamanho(self, valor: int):
        if valor >= 20 and valor <= 50:
            if valor%2 == 1:
                print("A chinela é de tamanho: ",valor,":",valor + 1)
                self.__tamanho = valor
                break
            else:
                if valor == 20:
                    print("A chinela é do tamanho", valor)
                print("A chinela é de tamanho: "valor - 1 ":"valor)
                break
        else:
            print("Valor invalido, digite novamente:")
chinelo = Chinela()
while chinelo.getTamanho() == 0:
    print("Digite o tamanho da chinela: ")
    valor = int(input())
    chinelo.setTamanho(valor)
print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())