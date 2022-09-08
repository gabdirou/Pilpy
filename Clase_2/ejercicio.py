menu = ("MENÚ\n 1 - Depósito\n 2 - Extracción\n 3 - Transferencias\n 4 - Salir")

print(menu) 


while True:
    try:
        seleccione = int(input("seleccione una opción: "))
        if seleccione >=1 and seleccione < 4 :
            monto = int(input("Ingrese monto: "))
            respuesta = input("¿Desea realizar otra operación? \n Ingrese S o N: ").upper()
            if respuesta == "S":
                print(menu)
                print(seleccione)
            else:
                print("Gracias por elegirnos")
                break      
        elif seleccione == 4 :
            print("Gracias por elegirnos")
            break
        else:
            print("Por favor, ingrese una opción válida")
    except:
        print("Por favor, ingrese una opción válida")