import random as rand

class Hero:
    def __init__(self, name, hp, max_hp, strength, lvl, inventory):
        self.name = name
        self.hp = hp
        self.maxhp = max_hp
        self.strength = strength
        self.lvl = lvl
        self.inventory = inventory
    
    def __str__(self):
        return """
        -------------
        Name: {}
        Hp: {}
        Damage: {}
        -------------""".format(self.name, self.hp, self.strength)

class Item():
    def __init__(self,name,atk):
        self.name = name
        self.atk = atk



def main():
    hero_is_alive = True
    hero = Hero("Jonas", 100, 100, rand.randint(1,10),1, [] )
    print(hero)
    print("Inventory=")
    print(hero.inventory)

    while True:
        val = input(
            "vilken dörr vill du välja? vänster [V], höger [H], eller rakt fram [F]")
        
        
        if val == "h":
            slumptal = rand.randint(1, 3)
            if slumptal == 1:
                print("Du fann en kista")
            elif slumptal == 2:
                print("Du måste möta ett monster")
            else:
                print("Atans du gick in i en fälla")
        
        
        elif val == "v":
            slumptal = rand.randint(1, 3)
            if slumptal == 1:
                print("Du fann en kista")
            elif slumptal == 2:
                print("Du måste möta ett monster")
            else:
                print("Atans du gick in i en fälla")
        
        
        elif val == "f":
            slumptal = rand.randint(1, 3)
            if slumptal == 1:
                print("Du fann en kista")
            elif slumptal == 2:
                print("Du måste möta ett monster")
            else:
                print("Atans du gick in i en fälla")

main()





