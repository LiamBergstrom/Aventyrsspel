class Duel:
    def duel(combatant_1, combatant_2):
        if combatant_1.strength>combatant_2:
            print(f"{combatant_1.name} wins")
            combatant_2.hp -= 1
        else:
            print(f"{combatant_2.name} wins")
            combatant_1.hp -= 1

        return combatant_1, combatant_2           
