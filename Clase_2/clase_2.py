#Condicionales en python
#Py lee secuencialmente las líneas de código, es decir de arriba hacia abajo
a = 3
b = 2
c = 5
r = a + b
print(r)
type(r)

##para que no lea todo y controlar qué es lo que va sucediendo por ejemplo los IF
if a >=0 :
    print(a)

if a > b :
    print("A es mayor a B")
    if a > c :
        print("a > c > b") 
else :
    print("B es mayor que A")    

if a == 3 :
    print("a = 3")
else :
    print("dif")

if a == "3" :
    print("a = 3")
else :
    print("dif")

edad_juan = 16

if edad_juan >= 16 and edad_juan >=18 :
    print("Juan puede votar y es mayor de edad")
else:
    print("No se cumple alguna de las condiciones")

if edad_juan >= 16 or edad_juan >=18 :
    print("Juan puede votar y es mayor de edad") # en este caso según el comando está bien pero lo que se declara está mal
    #juan no es mayor de edad ###Ojo
else:
    print("No se cumple alguna de las condiciones")
    
#Elif
a = 5
b = 6
c = 7
if a == 3:
    print("A es igual a 3")
elif a == 4:
    print("A es igual a 4")
elif a == 5:
    print("A es igual a 5")
else:
    print("A no es igual a nada")
