import random
INVVENTARIO = {"Pociones":3 , "Monedas": 150 , "Flechas": 30}

potions = 3
monedas = 150
espada  = 0
seleccion = ""
resultado = 0


INVVENTARIO.update({"Espada" : espada})


while True:
    resultado = random.randint(1, 3)
    print(resultado)



    Seleccion = input("Deseas toamr posion o  lootear (P L): ")

    if Seleccion == "P" and potions > 0:
        potions = potions - 1
        INVVENTARIO.update({"Pociones" : potions})
    elif Seleccion == "P" and potions == 0:
        print("no  tienes mas pociones")
    elif Seleccion == "L" and  resultado == 1:
            monedas = monedas   + 50
            INVVENTARIO.update({"Monedas" : monedas})
    elif Seleccion == "L" and resultado == 2:
        espada = espada + 1
        INVVENTARIO.update({"Espada" : espada})
    elif Seleccion == "L" and resultado == 3:
        potions = potions  + 1
        INVVENTARIO.update({"Pociones": potions})

    for key , value in INVVENTARIO.items():
        print(f"{key} : {value}")
