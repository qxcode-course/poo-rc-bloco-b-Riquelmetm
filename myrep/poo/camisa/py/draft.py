class Camisa:
    def __init__(self): # isso é o construtor em python
        self.__tamanho: str = "" # atributos em python com __ na frente são privados

    def getTamanho(self) -> str: # métodos em python tem self como primeiro atributo
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor != "P" and valor != "PP" and valor != "M" and valor != "G" and valor != "GG" and valor != "XG":
            print("Valores permitidos: PP, P, M, G, GG, XG.")
        else:
            self.__tamanho = valor


# loop principal
roupa = Camisa() # crian1do roupa com valor tamanho padrão
while roupa.getTamanho() == "": # mantendo usuário no loop
    print("Digite seu tamanho de roupa")
    tamanho: str = input()
        print("$" + line)
        args: list[str] = tamanho.split(" ")
    roupa.setTamanho(tamanho) # tentando atribuir e disparando erros

print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())