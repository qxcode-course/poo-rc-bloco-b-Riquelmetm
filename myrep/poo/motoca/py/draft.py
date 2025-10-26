class Pessoa:

    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade  
    

    def __str__(self) -> str:
        return f'{self.getName()}:{self.getIdade()}'

    def getName(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
class Moto:
    def __init__(self, nome: str):
        self.pessoa: Pessoa | None = None
        self.potencia = 1
        self.tempo = 0

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return False

        self.pessoa = pessoa
        return True

def remover(self) -> Pessoa | None:
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return None
        
        aux = self.pessoa
        self.pessoa = None
        return aux
def buytime (self, time: int):
    self.tempo += tempo

def drive (self, time: int):
    if self.tempo ==0:
        print("fail: buy time first")
        self.tempo = 0
        return
    if self.pessoa is None:
        print("fail: empty motorcycle")
        return
    if self.pessoa.getIdade() > 10:
        print("fail: too old to drive")
        return
    if time > self.time:
        time_driven = self.time
        self.time = 0
        print(f"fail: time finished after {time_driven} minutes")
    else:
        self.time -= time



def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line )
        args= line.split("")
        if args[0]=="end":
            break
        elif args[0]=="show":
        elif args[0]=="init":
        elif args[0]=="enter":
        elif args[0]=="leave":
        elif args[0]=="buy":
        elif args[0]=="drive":
        elif args[0]=="honk":



main()
# moto = Moto()
# moto.inserir(Pessoa("fulano"))
# print(moto.pessoa)


