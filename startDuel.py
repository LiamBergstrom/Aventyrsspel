def startDuel(combatant_1, combatant_2):
    print("Du möter en ", combatant_2)

    print("Här är ditt inventory")
    if len(combatant_1.inventory) == 0:
        print("Du har inga items i ditt inventory och du får använda dina fighting skills")
        
    else:
        for item in combatant_1.inventory:
            print(item.name)
        vapen_val = input("Välj ett vapen från ditt inventory och skriv dess namn exakt :")
        for item in combatant_1.inventory:
            if vapen_val == item.name:
                duell_styrka = combatant_1.strength + item.atk

    

# Här jämförs stats
    if duell_styrka>combatant_2.desc:
        print(f"{combatant_1.name} vann eftersom den hade mer attack points")
        combatant_2.hp -= 1
    else:
        print(f"{combatant_2.name} vann eftersom den hade mer attack points")
        combatant_1.hp -= 1

    return combatant_1, combatant_2           
