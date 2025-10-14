class Pessoa(self, nome: str):
    self.nome = nome
    
class Moto:
    def __init__(self, nome: str):
        sef.pessoa: Pessoa | None = None #pessoa pode ser pessoa ou pode ser nulo

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.pessoa != None:
            print("já tem gente na moto")
            return True

        self.pessoa = pessoa
        return False

    def remover(self) -> Pessoa | None:
        aux = self.pessoa
        self.pessoa = None
        return aux

def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line )
        args= line.split("")
        if args[0]=="end":
            break
        elif args[0]=="show":



main()
# moto = Moto()
# moto.inserir(Pessoa("fulano"))
# print(moto.pessoa)


