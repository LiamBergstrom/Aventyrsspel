class Items ():
    def __init__(self,name,atk):
        self.name = name
        self.atk = atk
        
    def __str__(self):
        return (self.name + " med " + str(self.atk) + " attack")

Yxa = Items("Yxa",7 )
Svärd = Items("Svärd", 5)
Pilbåge = Items("Pilbåge", 4)
Stick = Items("stick", 1)
Torch = Items("Torch", 2)


lista_med_items = [Yxa, Svärd, Pilbåge, Stick, Torch]