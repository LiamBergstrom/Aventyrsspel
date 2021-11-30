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

class Items ():
    def __init__(self,name,atk):
        self.name = name
        self.atk = atk
        
    def __str__(self):
        return (self.name + " med " + str(self.atk) + " attack")

dunder_yxa = Items("Yxa",7 )
svärd = Items("Svärd", 5)
pilbåge = Items("Pilbåge", 4)
pokeball = Items("pokeball", 3)
gucci_belt_with_ultimate_whip_power = Items("gucci-belt", 2)

lista_med_items = [dunder_yxa, svärd, pilbåge, pokeball, gucci_belt_with_ultimate_whip_power]

class Potions ():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return (self.name + "med" + str(self.hp) + "hp")

        
trevlig_läskeblask = Potions("potion", 2)
cedevita = Potions("cedevita",3)
sicko_pot = Potions("sicko_pot", 5)

class Monster ():
    def __init__(self, name, desc, hp):
            self.name = name
            self.desc = desc
            self.hp = hp
        
    def __str__(self):
        return (self.name + " " + self.desc)

läskigt_monster = ("läskigt_monster", 5, 3)
strongman = ("strongman", 10, 2)
snubbesomgårtibble = ("tibblesnubbe", 4, 1)

lista_med_monster = [läskigt_monster, strongman,snubbesomgårtibble]

class traps():
    def __init__(self, name, desc, dmg):
        self.name = name
        self.desc = desc
        self.dmg = dmg
    
    def __str__(self):
        return (self.name + " " + self.desc + " " + self.dmg)

sätt_dig_ner = ("Ett mörkt rum med en stol öppnas, Du funderar och klurar men blir tillslut så trött att du måste sätta dig ner och vila, BAAM! Golvet faller in och du faller till din död i en stor bunt med spikar", 100)
fontänen = ("Du möts av en fontän, fontänen ser väldigt lovande ut så du tar ett dopp, Plask du blir nerdragen och nästan drunkar men du klarar dig", 4)

def main():
    hero_is_alive = True
    hero = Hero("Jonas", 100, 100, rand.randint(1,10),1, [] )
    print(hero)
    print("Inventory = ", hero.inventory)
    
    while True:
        val = input(
            "Vad vill du göra?, Öppna inventory[i], Börja utforska,[u] Kolla dina stats,[s]")
        if val == "i":
            print("Ditt inventory består av = ", hero.inventory)

        elif val == "u":
            val = input
            print("Vilken dörr vill du väljas? vänster [v], höger [h], eller rakt fram [f]")
            if val == "h" or val == "v" or val == "f":
                slumptal = rand.randint(1, 3)
            if slumptal == 1:
                print("Du fann en kista")
                val = input(
            "Vill du öppna kistan? du har inget val. skriv [ja]")
            if val == "ja":
                hero.inventory.append(rand.choice(lista_med_items))
                print("Du hittade en", hero.inventory[0])
            elif slumptal == 2:
                print("Du måste möta ett monster, monstret är: ")
                rand.choice(lista_med_monster)
                print("Du tog {dmg} skada men fortsätter vidare...")
            else:
                print("Atans du gick in i en fälla")        

main()

