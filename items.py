#
#
#
#from TRPGMain import Protagonist

class Items:
    def __init__(self, Hpotion, Mpotion, Cloak, Dagger):
        self.Hpotion = Hpotion
        self.Mpotion = Mpotion
        self.Dagger = Dagger
        self.Cloak = Cloak
    
Items.Hpotion = 3
Items.Mpotion = 2
Items.Cloak = 0
Items.Dagger = 4

def Hpotion(Hpotion):
    Protagonist.HP = Protagonist.HP + Items.Hpotion
    