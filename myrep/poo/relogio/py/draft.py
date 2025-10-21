class Watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

    def getHora(self):
        return self.__hora

    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):
        return self.__segundo

    def setHora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def setMinuto(self, minuto: int):
        if minuto < 0 or minuto > 59:
            print("fail: minuto invalido")
            return
        self.__minuto = minuto

    def setSegundo(self, segundo: int):
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
            return
        self.__segundo = segundo

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto > 59:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0


def main():
    relogio = Watch()
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "show":
            print(relogio)

        elif args[0] == "set":
            hora, minuto, segundo = map(int, args[1:])
            relogio.setHora(hora)
            relogio.setMinuto(minuto)
            relogio.setSegundo(segundo)

        elif args[0] == "next":
            relogio.nextSecond()

        elif args[0] == "init":
            hora, minuto, segundo = map(int, args[1:])
            relogio = Watch(hora, minuto, segundo)

        elif args[0] == "end":
            break


main()
