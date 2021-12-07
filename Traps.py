class Traps(): 
    def __init__(self, name, desc, dmg):
        self.name = name
        self.desc = desc
        self.dmg = dmg
    
    def __str__(self):
        return (self.name + " " + self.desc + " " + self.dmg)

Sätt_dig_ner = Traps("Sätt dig ner" , "Du möts av ett mörkt rum vad vill du göra? Fortsätta och gå in i rummet eller gå där ifrån", 100)
val = input(
    "Vill du fortsätta? [f] eller gå där ifrån [g]")
if val == "f":
    print("Du fortsätter in och möts av en stol, Vill du sätta dig på den? [ja], eller [nej]")
    # såhär används damage om man gör val   print(Sätt_dig_ner.dmg)

elif val == "g": 
    print("Du går där ifrån")

        
            
            

Fontänen = Traps("Fontänen", "Du möts av en fontän, fontänen ser väldigt lovande ut så du tar ett dopp, Plask du blir nerdragen och nästan drunkar men du klarar dig", 4)
Snygg_gäri = Traps("Snygg_gäri", "Du stöter på en snygg gäri. Du säger en dålig pick-up line och på grund av det tar hon fram en Glock 18 och skjuter dig i benet.", 6)

lista_med_traps = [Sätt_dig_ner, Fontänen, Snygg_gäri]