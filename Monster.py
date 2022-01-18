class Monster ():
    def __init__(self, name, desc, hp):
        self.name = name
        self.desc = desc
        self.hp = hp

    def __str__(self):
        return (self.name + " med " + str(self.desc) + " attack och " + str(self.hp) + " hp.")


Gremling = Monster("Gremling", 5, 3)
Golaja = Monster("Golaja", 10, 2)
Yxcha = Monster("Yxcha", 4, 1)
Jojames = Monster("Jojames", 5, 10)
Drakkar = Monster("Drakkar", 7, 5)


lista_med_monster = [Gremling, Golaja, Yxcha, Jojames, Drakkar]
