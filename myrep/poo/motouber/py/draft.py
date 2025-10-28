class Pessoa:
  def __init__(self, name, din):
    self.__name = name
    self.__din = din

    def getName(self):
        return self.__name
    def getDin(self):
        return self.__din

    def __str__(self):
        return f"{self.getName()}:{self.getDin()}"

    def receber (self, dinheiro: int):
        self.dinheiro += dinheiro

    def gastar(self,dinheiro:int):
        if dinheiro <= self.__din:
            self.__din -= dinheiro
        else:
            pago = self.__din
            self.__din = 0
            return pago

    
class Moto:
    def __init__(self):
        self.custo = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None
    def __str__(self):
        return f"Cost: {self.custo}: Driver: {getmotorista()}: Passenger: {getpassageiro()}"


    def subirmoto(self, pessoamoto):

        self.__motorista = pessoamoto

    def descermoto(self):
        if self.__motorista is None:
            print("fail: nao tem motorista")
            return
        self.__motorista = None

    def subirpass(self, passageiro: Pessoa):
        if self.__passageiro is not None:
            print("fail: tem passageiro")
            return

        if self.__motorista is None:
            print("fail: no  driver")

        self.__passageiro = passageiro
        self.custo = 0



    def descerpass(self):
        if self.__passageiro is none:
            print("no passenger to leave")
            return

        pass_obj = self.__passageiro
        driver_obj = self.__motorista
        custo_total = self.custo

        valor_pago = pass_obj.gastar(custo_total)

        if valor_pago < custo_total:
            print("fail: Passenger does not have enough money")

        driver_obj.receber(custo_total)

        print(f"{pass_obj.getName()}:{pass_obj.getDin()} left")

        self.__passageiro = None
        self.custo = 0
    
    def andar(self, km:int):
        if self.__motorista is None:
            print("fail: no drive to drive")
            return
        
        if self.__passageiro is not None:
            self.custo += km
    
moto = Moto()
while True:
    line = input()
    print("$" + line)
    args = line.split()
    op = args[0]
    if op == "end":
        break
    elif op == "show":
        print(moto)
    elif op == "setDriver":
        nome = args[10]
        dinheiro = int(args[2])
        motorista = Pessoa(nome, dinheiro)
        moto.subirmoto(motorista)
    elif op == "setPass":
        nome = args[1]
        dinheiro = int(args[2])
        passageiro = Pessoa(nome, dinheiro)
        moto.subirpass(passageiro)

    elif op == "drive":
        km = int(args[1])
        moto.andar(km)
    
    elif op == "LeavePass":
        moto.descerpass()
    
    else: print (f"fail: error invalid command")