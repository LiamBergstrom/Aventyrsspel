class Potions ():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return (self.name + " med " + str(self.hp) + " hp")

        
Trevlig_läskeblask = Potions("potion", 2)
Cedevita = Potions("cedevita",3)
Sicko_pot = Potions("sicko_pot", 5)

lista_med_potions = [Trevlig_läskeblask, Cedevita, Sicko_pot]