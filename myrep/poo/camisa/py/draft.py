class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor != "P" and valor != "PP" and valor != "M" and valor != "G" and valor != "GG" and valor != "XG":
            print("Valores permitidos: PP, P, M, G, GG, XG.")
        else:
            self.__tamanho = valor


roupa = Camisa() 
while roupa.getTamanho() == "":
    print("Digite seu tamanho de roupa")
    tamanho: str = input()
    roupa.setTamanho(tamanho) 
print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())