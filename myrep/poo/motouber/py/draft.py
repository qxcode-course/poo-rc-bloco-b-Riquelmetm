class Pessoa:
  def __init__(self, name, din):
    self.__name = name
    self.__din = din

    def getName(self):
        return f"{self.__name}"
    def getDin(self):
        return f"{self.__din}"

    def __str__(self):
        return f"{self.getName()}:{self.getdin()}"

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
        self.motorista = None
        self.passageiro = None
    def __str__(self):
        return f"Cost: {self.custo}: Driver: {self.motorista}: Passenger: {self.passageiro}"
    


    