class Watch:
    def __init__(self, hora:int, minuto:int, segundo:int):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0

    def getHora(self):
        return self.__hora
    def setHora(self, hora: int):
        if hora < 0 or hora > 23:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def setminuto (self, minuto:int):
        if minuto > 59 or minuto < 0:
            print("fail: minuto invalida")
            return
        self.__minuto = minuto
        
    def setsegundo (self, segundo:int)

    def __str__(self):
        return f"{self.__hora}:{self.__minuto}:{self.__segundo}"
        

relogio = Watch(111,0,0)

relogio.__hora = 89797
print(relogio)
relogio.setHora(6)
# print(relogio.getHora())

print(relogio)