def Saldo(SaldoActual):
    print(f"Su saldo actual es de $ {SaldoActual}")


def Depositar():
    CantidadValida = False
    while CantidadValida == False:

        Cantidad = float(input("Ingrese Cantidad de deposito: "))

        if Cantidad <= 0:
            print("Esa cantidad no es validad")
        else:

            CantidadValida = True
            return Cantidad

def Retirar(SaldoActual):
    CantidadValida = False
    while CantidadValida == False:

        Cantidad = float(input("Ingrese Cantidad de retiro: "))

        if  Cantidad > SaldoActual or Cantidad < 0:
            print("Esa cantidad no es validad")
        else:

            CantidadValida = True
            return Cantidad





def main():
    SaldoTotatl = 100.00
    IsRuning = True

    while IsRuning == True:
        print("****************Bank Menu****************")
        print("1.Mostrar Saldo")
        print("2.Depositar")
        print("3.Retirar")
        print("4.Salir")

        eleccion = int(input("Elija una opcion: "))
        if eleccion == 1:
            print("*****************************************")
            Saldo(SaldoTotatl)

        elif eleccion == 2:
            print("*****************************************")
            Cantidad = Depositar()
            SaldoTotatl = SaldoTotatl + Cantidad
        elif eleccion == 3:
            print("******************************************")
            Cantidad = Retirar(SaldoTotatl)
            SaldoTotatl = SaldoTotatl - Cantidad
        elif eleccion == 4:
            IsRuning = False
            print("**************Tenga buen dia*************")




if __name__ == "__main__":
    main()
