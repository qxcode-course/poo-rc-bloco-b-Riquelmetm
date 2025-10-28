class Grafite:
    def __init__ (self, grossura: float, dureza: str, tamanho: int):
        self.grossura = grossura
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
        return 0 
    
    def __str__(self) -> str:
        return f"[{self.grossura}:{self.dureza}:{self.tamanho}]"


class Lapiseira:
    def __init__(self, grossura: float):
        self.grossura = grossura
        self.ponta = None

    def inserir(self, grafite_novo: Grafite):
        if self.ponta is not None:
            print("fail: ja existe grafite")
            return

        if self.grossura != grafite_novo.grossura:
            print("fail: calibre incompativel")
            return
        
        self.ponta = grafite_novo

    def remover(self):
        if self.ponta is None:
            print("fail: nao existe grafite")
            return
        
        self.ponta = None
        
    def __str__(self) -> str:
        ponta_str = str(self.ponta) if self.ponta is not None else "null"
        return f"calibre: {self.grossura}, grafite: {ponta_str}"

    def escrever(self):
        if self.ponta is None:
            print("fail: nao existe grafite")
            return
        
        if self.ponta.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        
        gasto = self.ponta.GastoPorFolha()
        
        if gasto == 0:
            print("fail: dureza invalida, nao gasta")
            return

        tamanho_final = self.ponta.tamanho - gasto

        if tamanho_final < 10:
            self.ponta.tamanho = 10
            print("fail: folha incompleta")
        else:
            self.ponta.tamanho = tamanho_final


def main():
    lapiseira = None

    while True:
        linha = input()
        command = linha.split()
        
        print(f"${linha}")


        op = command[0]
        
        if op == 'end':
            break
        
        elif op == 'init':
            lapiseira = Lapiseira(float(command[1]))
        
        elif lapiseira is None and op not in ['end', 'init']:
            print("fail: lapiseira nao foi iniciada")
            continue
        
        elif op == 'insert':
            grafite = Grafite(float(command[1]), command[2], int(command[3]))
            lapiseira.inserir(grafite)
        
        elif op == 'remove':
            lapiseira.remover()

        elif op == 'write':
            paginas = 1
            if len(command) > 1:
                paginas = int(command[1])
            
            for _ in range(paginas):
                lapiseira.escrever()

        elif op == 'show':
            print(lapiseira)
        
        else:
            print("fail: comando invalido")

main()