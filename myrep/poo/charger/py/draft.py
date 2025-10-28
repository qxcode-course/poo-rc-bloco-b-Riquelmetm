class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCarga(self):
        return self.__carga

    def getCapacidade(self):
        return self.__capacidade

    def descarregar(self, valor):
        self.__carga = max(0, self.__carga - valor)

    def carregar(self, valor):
        self.__carga = min(self.__capacidade, self.__carga + valor)


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__min_uso = 0
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def show(self):
        parts = [f"Notebook: {'ligado por ' + str(self.__min_uso) + ' min' if self.__ligado else 'desligado'}"]
        if self.__carregador:
            parts.append(f"Carregador {self.__carregador.getPotencia()}W")
        if self.__bateria:
            parts.append(f"Bateria {self.__bateria.getCarga()}/{self.__bateria.getCapacidade()}")
        print(", ".join(parts))

    def turn_on(self):
        if self.__carregador or (self.__bateria and self.__bateria.getCarga() > 0):
            self.__ligado = True
            return
        print("fail: não foi possível ligar")

    def turn_off(self):
        self.__ligado = False

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        for _ in range(tempo):
            if self.__carregador and self.__bateria:
                self.__bateria.carregar(self.__carregador.getPotencia())
            elif self.__bateria:
                if self.__bateria.getCarga() > 0:
                    self.__bateria.descarregar(1)
                else:
                    print("fail: descarregou")
                    self.__ligado = False
                    return
            self.__min_uso += 1

    def set_battery(self, capacidade: int):
        if self.__bateria is not None:
            print("fail: bateria já conectada")
            return
        self.__bateria = Bateria(capacidade)

    def rm_battery(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        bat = self.__bateria
        print(f"Removido {bat.getCarga()}/{bat.getCapacidade()}")
        self.__bateria = None
        if not self.__carregador:
            self.__ligado = False
        return bat

    def set_charger(self, potencia: int):
        if self.__carregador:
            print("fail: carregador já conectado")
            return
        self.__carregador = Carregador(potencia)

    def rm_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        pot = self.__carregador.getPotencia()
        print(f"Removido {pot}W")
        self.__carregador = None
        if self.__bateria is None:
            self.__ligado = False


notebook = Notebook()

while True:
    command = input().split()
    print(f"${' '.join(command)}")

    if command[0] == "end":
        break
    elif command[0] == "show":
        notebook.show()
    elif command[0] == "turnOn":
        notebook.turn_on()
    elif command[0] == "turnOff":
        notebook.turn_off()
    elif command[0] == "use":
        notebook.use(int(command[1]))
    elif command[0] == "setBat":
        notebook.set_battery(int(command[1]))
    elif command[0] == "rmBat":
        notebook.rm_battery()
    elif command[0] == "setCharger":
        notebook.set_charger(int(command[1]))
    elif command[0] == "rmCharger":
        notebook.rm_charger()
