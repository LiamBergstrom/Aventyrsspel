class Monster ():
    def __init__(self, name, desc, hp):
            self.name = name
            self.desc = desc
            self.hp = hp
    
    def __str__(self):
        return (self.name + " med " + str(self.desc) + " attack och " + str(self.hp) + " hp")

Gremling = Monster("gremling", 5, 3)
Golaja = Monster("golaja", 10, 2)
Yxcha = Monster("yxcha", 4, 1)

lista_med_monster = [Gremling, Golaja, Yxcha]