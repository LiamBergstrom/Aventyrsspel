import random as rand

while True:
    val = input(
        "vilken dörr vill du välja? vänster [V], höger [H], eller rakt fram [F]")
    if val == "h":
        slumptal = rand.randint(1, 3)
        if slumptal == 1:
            print("Du fann en kista")
        elif slumptal == 2:
            print("Du måste möta ett monster")
        else:
            print("Atans du gick in i en fälla")
    elif val == "v":
        slumptal = rand.randint(1, 3)
        if slumptal == 1:
            print("Du fann en kista")
        elif slumptal == 2:
            print("Du måste möta ett monster")
        else:
            print("Atans du gick in i en fälla")
    elif val == "f":
        slumptal = rand.randint(1, 3)
        if slumptal == 1:
            print("Du fann en kista")
        elif slumptal == 2:
            print("Du måste möta ett monster")
        else:
            print("Atans du gick in i en fälla")
