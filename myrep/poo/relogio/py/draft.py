class Watch:
    def __init__(self, hora:int, minuto:int, segundo:int):
        self.__hora = 0
        self.setHora(hora)
        self.__minuto = 0
        self.setMinuto(minuto)
        self.__segundo = 0
        self.setSegundo(segundo)

    def __str__(self):
        return f"{self.__hora}:{self.__minuto}:{self.__segundo}"

    def getHora(self):
        return self.__hora

    def setHora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def setMinuto (self, minuto:int):
        if minuto > 59 or minuto < 0:
            print("fail: minuto invalida")
            return
        self.__minuto = minuto

    def setSegundo (self, segundo:int)
        if segundo < 0 or segundo > 59:
            print("fail: segundo invalido")
            return
        self.__segundo = segundo

    

        

relogio = Watch()