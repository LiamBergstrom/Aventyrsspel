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
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
    
    def __str__(self):
        return (self.name + " " + self.desc)

dunder_yxa = Items("Yxa",7 )
svärd = Items("Svärd", "(+5 attack)")
trevlig_läskeblask = Items("potion", " +3 {hp}")
pilbåge = Items("Pilbåge", "+4 attack")
pokeball = Items("pokeball", "(+3 attack)")
gucci_belt_with_ultimate_whip_power = Items("gucci-belt", "(+2 attack")

lista_med_items = [dunder_yxa, svärd, trevlig_läskeblask, pilbåge, pokeball, gucci_belt_with_ultimate_whip_power]

class Monster ():
    def __init__(self, name, desc, hp):
            self.name = name
            self.desc = desc
            self.hp = hp
        
    def __str__(self):
        return (self.name + " " + self.desc)

läskigt_monster = ("läskigt_monster","(+5 attack)","3hp")
strongman = ("strongman","(+10 attack)","2hp")
snubbesomgårtibble = ("tibblesnubbe","(+4 attack)", "1hp")

lista_med_monster = [läskigt_monster, strongman,snubbesomgårtibble]




def main():
    hero_is_alive = True
    hero = Hero("Jonas", 100, 100, rand.randint(1,10),1, [] )
    print(hero)
    print("Inventory = ", hero.inventory)
    

    while True:
        val = input(
            "vilken dörr vill du välja? vänster [V], höger [H], eller rakt fram [F]")
        
        
        if val == "h" or val == "v" or val == "f" :
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

