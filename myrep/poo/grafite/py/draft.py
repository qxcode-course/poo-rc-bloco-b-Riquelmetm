class Lead:
    def __init__ (self,  thickness: int, size: int, hardness: str):
        self.thickness = 0
        self. size = 0
        self.hardness = ""
    
    def usagerPerSheet (self):
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        elif self.hardness == "6B":
            return 6
    