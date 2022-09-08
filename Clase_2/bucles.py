lista = []
# For
for i in "Python":
    print(i)

#For i in range (inicio, salida): #la función no toma el último valor
for i in range(0,10):
    print(i)

for i in range(0,10,2): #el tercer elemento indica el salto que quiere darse
    print(i)

for i in range(0,10):
    lista.append(i)

#lista = []
#for i in range(10):
#numero_usuario = int(input("Ingrese un número: "))
 #   lista.append(numero_usuario)
#print(lista)
#    dato_ingreso = input("Ingrese un número: ")
    
#Validación
#if dato_ingreso.isnumeric():
#        lista.append(int(dato_ingreso))
#else: 
#    print("No es un número")
        
#print(lista)

#While

x = 10
while x < 0 :
    print(x)
    x -= 1

#si se imprime este código no va a parar de correrlo porque no se establece un brake
#while x < 0 :
#    print(x)