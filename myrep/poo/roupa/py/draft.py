class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor != "P" and valor != "PP" and valor != "M" and valor != "G" and valor != "GG" and valor != "XG":
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        else:
            self.__tamanho = valor
    

roupa = Camisa() 
while True:
    line: str = input()
    print("$" + line)
    args: list[str] = line.split()
    if args[0] == "show":
        print(f"size: ({roupa.getTamanho()})")
    if args[0] == "size":
        tamanho = args[1]
        roupa.setTamanho(tamanho)
    if args[0] == "end":
        break
    
        
