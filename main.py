import random as rand
from encounterTrap import encounterTrap
from startDuel import startDuel
from Hero import *
from Monster import *
from Potions import *
from Items import *
from Traps import *


def main():
    hero_is_alive = True
    hero = Hero("Hero", 100, 100, rand.randint(1, 10), 1, [])
    print(hero)
    print("Inventory = ", hero.inventory)

    while hero_is_alive:

        val = input(
            "Vad vill du göra?, Öppna inventory[i], Börja utforska,[u] Kolla dina stats,[s] ->")
        if val == "i":
            if len(hero.inventory) == 0:
                print("Du har inga items i ditt inventory.")
            print("Ditt inventory består av = ")
            for x in hero.inventory:
                print(x.name, x.atk, x.desc)

        elif val == "s":
            print(hero)

        elif val == "u":
            val = input(
                "Vilken dörr vill du väljas? vänster [v], höger [h], eller rakt fram [f] ->")

            if val == "h" or val == "v" or val == "f":
                slumptal = rand.randint(1, 3)
                if slumptal == 1:
                    print("Du fann en kista.")
                    val = input(
                        "Vill du öppna kistan? [ja] [nej] ->")
                    if val == "ja":
                        hero.inventory.append(rand.choice(lista_med_items))
                        print("Du hittade en", hero.inventory[-1])
                    elif val == "nej":
                        print("Du fortsätter vidare som en idiot utan items.")

                        # man skulle kunna skriva att en kista är rotten eller lyser guld

                elif slumptal == 2:
                    print("Du måste möta ett monster, monstret är: ")
                    monster = rand.choice(lista_med_monster)
                    print(monster)
                    print("Det här är dina stats: ")
                    print(hero)

                    val = input(
                        "Vill du engage combat [k] eller försöka springa ifrån [s] ->")

                    if val == "k":
                        (hero, monster) = startDuel(hero, monster)
                    elif val == "s":
                        print("Du gick därifrån.")
                else:
                    print("Atans du gick in i en fälla.")
                    trap = rand.choice(lista_med_traps)

                    val = input("Tryck [k] för att se vad som händer nu ->")
                    if val == "k":
                        encounterTrap(hero, trap)

        if hero.hp < 1:
            hero_is_alive = False


main()
