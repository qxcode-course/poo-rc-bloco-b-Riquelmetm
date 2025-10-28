class Pessoa:
  def __init__(self, name, din):
    self.__name = name
    self.__din = din

    def getName(self):
        return f"{self.__name}"
    def getDin(self):
        return f"{self.__din}"

    def __str__(self):
        return f"{self.getName()}:{self.getDin()}"

    def receber (self, dinheiro: int):
        self.dinheiro += dinheiro

    def gastar(self,dinheiro:int):
        if dinheiro <= self.dinheiro:
            self.dinheiro -= dinheiro
        else:
            pago = self.dinheiro
            self.dinheiro = 0
            return pago

    
class Moto:
    def __init__(self):
        self.custo = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
    def __str__(self):
        return f"Cost: {self.custo}: Driver: {getmotorista()}: Passenger: {getpassageiro()}"
    def subirmoto(self, pessoamoto):
        if self.__motorista is not None:
            print("fail: no driver")
            return
        self.__motorista = pessoamoto

    def descermoto(self):
        if self.__motorista is None:
            print("fail: nao tem motorista")
        self.__motorista = None

    def subirpass(self, passageiro):
        if self.__passageiro is not None:
            print("fail: tem passageiro")
            return
        if self.__motorista is None:
            print("fail: no  driver")

        self.__passageiro = passageiro
        self.custo = 0
