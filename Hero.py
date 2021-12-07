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