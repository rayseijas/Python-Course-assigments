import random



def Chequeo(SelecionAc, SelecionAf, Selecion, fila_random, fila_random2, fila_random3, columna_random, columna_random2,
            columna_random3, Bombas, vida, Ganar):
    if SelecionAc == columna_random and SelecionAf == fila_random and Selecion == "A":
        vida = False
    elif SelecionAc == columna_random2 and SelecionAf == fila_random2 and Selecion == "A":
        vida = False
    elif SelecionAc == columna_random3 and SelecionAf == fila_random3 and Selecion == "A":
        vida = False
    elif SelecionAc == columna_random and SelecionAf == fila_random and Selecion == "M":
        Bombas = Bombas - 1
        if Bombas == 0:
            Ganar = True
    elif SelecionAc == columna_random2 and SelecionAf == fila_random2 and Selecion == "M":
        Bombas = Bombas - 1
        if Bombas == 0:
            Ganar = True
    elif SelecionAc == columna_random3 and SelecionAf == fila_random3 and Selecion == "M":
        Bombas = Bombas - 1
        if Bombas == 0:
            Ganar = True


    return vida, Bombas, Ganar


Bombas = 3
marcadores = 4
Ganar = False
vida = True
Fila = ["#", "#", "#", "#", "#", "#", "#", "#"]
columna1 = ["#", "#", "#", "#", "#", "#", "#", "#"]
columna2 = ["#", "#", "#", "#", "#", "#", "#", "#"]
columna3 = ["#", "#", "#", "#", "#", "#", "#", "#"]
columna4 = ["#", "#", "#", "#", "#", "#", "#", "#"]
Mapa = [Fila, columna1, columna2, columna3, columna4]

print("Bienvenido a busca minas, para ganar debe marcar las 3 bombas escondidas con (!) ¡Buena suerte!")

# Generación de bombas al azar (se queda igual)
for i in range(1):  # Cambiado a 1 para que corra tus variables una sola vez
    fila_random = random.randint(0, 4)
    columna_random = random.randint(0, 7)
    fila_random2 = random.randint(0, 4)
    columna_random2 = random.randint(0, 7)
    fila_random3 = random.randint(0, 4)
    columna_random3 = random.randint(0, 7)

while Ganar == False and vida == True:
    for Map in Mapa:
        for Map2 in Map:
            print(Map2, end=" ")
        print()

    Selecion = input("Desea activar o marcar (A M): ")
    if Selecion == "A":
        SelecionAc = int(input("Ingrese el valor de la columna: "))
        SelecionAf = int(input("Ingrese el valor de la fila: "))
        SelecionAc = SelecionAc - 1
        SelecionAf = SelecionAf - 1
        Mapa[SelecionAf][SelecionAc] = " "
    elif Selecion == "M" and marcadores > 0:
        SelecionAc = int(input("Ingrese el valor de la columna: "))
        SelecionAf = int(input("Ingrese el valor de la fila: "))
        SelecionAc = SelecionAc - 1
        SelecionAf = SelecionAf - 1
        marcadores = marcadores - 1
        Mapa[SelecionAf][SelecionAc] = "!"
    elif Selecion == "M" and marcadores == 0:
        print("No puedes poner mas marcadores buenas suerte")
    else:
        print("Seleccion no existe")


    vida, Bombas, Ganar = Chequeo(SelecionAc, SelecionAf, Selecion, fila_random, fila_random2, fila_random3,
                                  columna_random, columna_random2, columna_random3, Bombas, vida, Ganar)

if Ganar == True:
    print('¡Has ganado!')
else:
    print('¡Has perdido! Pisaste una bomba.')
