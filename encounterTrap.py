import random as rand


def encounterTrap(hero, trap):

    slumptal = rand.randint(1, 3)
    if slumptal == 1:
        print("Du möts av ett mörkt rum vad vill du göra? Fortsätta och gå in i rummet eller gå där ifrån? ->")
        val = input("Vill du fortsätta? [f] eller gå där ifrån [g] ->")
        if val == "f":
            print("Du fortsätter in och möts av en stol.")
            val = input("Vill du sätta dig på den? [ja], eller [nej] ->")
            if val == "ja":
                print("När du sätter dig på stolen känner du hur svajig den är.")
                val = input(
                    "Vill du ställa dig upp och kanske förlora möjligheten att få en kista, eller vill du gå där ifrån? stanna[s]; eller gå [g] ->")
                if val == "s":
                    print("Du tar 100 Damage och du dör. Spelet avslutas.")
                    hero.hp -= 100

                if val == "nej":
                    print("Du sätter dig inte på stolen och går där ifrån.")

        elif val == "g":
            print("du går där ifrån")
            # såhär används damage om man gör val   print(Sätt_dig_ner.dmg)

    elif slumptal == 2:
        print("Du möts av en fontän, fontänen ser väldigt lovande ut så du tar ett dopp, Plask du blir nerdragen och nästan drunkar men du klarar dig och du tar 4 damage.")
        hero.hp -= 4

    elif slumptal == 3:
        print("Du stöter på en snygg maiden. Du säger en dålig pick-up line och på grund av det tar hon fram en Musket och skjuter dig i benet och du tar 6 damage.")
        hero.hp -= 6

        return hero
