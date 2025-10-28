class Grafite:
    def __init__ (self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho
    def GastoPorFolha (self):
        if self.dureza == "HB":
            return 1
        elif self.dureza == "2B":
            return 2
        elif self.dureza == "4B":
            return 4
        elif self.dureza == "6B":
            return 6

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.ponta = None