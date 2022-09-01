#variables
mensaje_usuario = input('Ingrese un mensaje: ')
print(mensaje_usuario)

x = int(input('Ingrese un numero: '))
y = int(input('Ingrese otro numero: '))

resultado = x + y
#input siempre toma como string x lo que en vez de sumar concatena los string
print('el resultado es', resultado)

print("El tipo de dato de X es: ", type(x))
print("l tipo de dato de Y es: ",type(y))

# x=str(x) esto lo convertiria en string

resultado = x * y
print('El resultado es -->', resultado)