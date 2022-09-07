menu = ("MENÚ\n 1 - Depósito\n 2 - Extracción\n 3 - Transferencias\n 4 - Salir")

print(menu) 


while True:
    seleccione = int(input("seleccione una opción: "))
    if type(seleccione) == int and seleccione >=1 and seleccione < 4 :
        monto = int(input("Ingrese monto: "))
        if type(monto) == int:
            respuesta = print(input("¿Desea realizar otra operación? \n Ingrese S o N: ")) 
            if respuesta == "S":
                print(menu)
                print(seleccione)
            else:
                print("Gracias por elegirnos")
                break      
        else:
            print("Por favor, ingrese una opción válida")
    elif seleccione == 4 :
        print("Gracias por elegirnos")
        break
    else:
        print ("Por favor, ingrese una opción válida")
        
