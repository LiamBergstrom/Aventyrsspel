class Items ():
    def __init__(self, name, atk, desc):
        self.name = name
        self.atk = atk
        self.desc = desc

    def __str__(self):
        return (self.name + " med " + str(self.atk) + " attack")


Axe = Items("Axe", 7, "Attack")
Sword = Items("Sword", 3, "Attack")
Bow = Items("Bow", 4, "Attack")
Stick = Items("Stick", 1, "Attack")
Torch = Items("Torch", 2, "Attack")
Longsword = Items("Longsword", 5, "Attack")
Flail = Items("Flail", 6, "Attack")
Sling = Items("Sling", 1, "Attack")

lista_med_items = [Axe, Sword, Bow, Stick, Torch, Longsword, Flail, Sling]
