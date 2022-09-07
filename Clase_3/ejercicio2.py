while True:
    try:
        x = int(input("ingrese un número entero: "))
        y = int(input("ingrese otro número entero: "))
        if  x == y :
            print("Por favor, ingrese números diferentes")
        elif x < y and x % 2 == 0 :
            for i in range(x+2, y, 2) :
                    print(i)
        elif x < y and x % 2 == 1 :
            for i in range(x, y, 2) :
                print(i+1)
        elif x > y and x % 2 == 0 :
            for i in range(y+2, x, 2) : 
                    print(i)
        else:
            for i in range(y, x, 2) : 
                    print(i+1)    
    except:
        print("Por favor, ingrese un número entero")
    respuesta = input("¿Desea continuar? S/N: ").upper()
    if respuesta == "N" :
        print("Vuelva pronto")
        break
    

    