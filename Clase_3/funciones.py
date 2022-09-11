#Nombre
#Argumento
#Código
#Retorno

#Se escribe con minuscula y los espacios con guión bajo (Buenas prácticas)

def sumar(a, b):
    resultado = a + b
    return resultado

resultado_suma = sumar(2, 3)
print(resultado_suma)
print(sumar(2, 3))

#Función 2. En este caso no solicita parámetros porque están explicitados
def resta():
    resultado = 2 - 3
    return resultado

print(resta())

#Función 3. Directamente larga el resultado porque ya se puso el print en la fórmula

def resta_2():
    print(2-3)
    return

resta_2()

#Es esperable que incluya un return una función, pero no es necesario.

#Funcion 4
#def saludo(nombre):
 #   print('Hola', nombre)

#nombre = input('Ingrese su nombre: ')
#saludo(nombre)
#nombre = input('Ingrese su nombre: ')
#saludo(nombre)

def saludo(cantidad_saludos):
    """La triple comilla se utiliza para documentar el propósito de las funciones


    Args:
        cantidad_saludos (int): cantidad de saludos

    Returns:
        Lista: personas saludadas
    """
    
    lista_nombres = []

    for i in range(cantidad_saludos):
        nombre = input('Ingrese su nombre: ')
        print('Hola', nombre)

        lista_nombres.append(nombre)
    
    #print(lista_nombres)
    return lista_nombres

#nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar: ')))
#Si yo pongo el comando print(lista_nombres) en esta línea, es decir, por fuera de la función definida, no lo tomará ya que es
#una variable local. Para llamarla por fuera se debe generar otra variable (como la "nombres" de arriba)

def prueba(a, b, c):
    print(a, b, c)

a = 420
b = 3
c = 5
prueba(b, c, a) #en este caso ejecuta, posicionalmente, en el orden que se pide (3,5,420), sin embargo, para la función b será a, c,
#  será b, y a, será c. Una forma de asegurar que no importe el orden, igualamos la variable.
prueba(b=b, c=c,a=a)

#En archivo limpio, tratar siempre de que las funciones queden arriba. Se puede crear archivos propios de funciones.
def orden(lista, sentido):
    """Esta función nos permite ordenar listas en base a un sentido determinado.
    
    Args:
        lista(list): lista genérica
        sentido(bool): Definir si la lista se ordena de mayor a menor o menor a mayor
    
    Returns:
        lista: lista ordenada
    """
    
    lista.sort(reverse=sentido)

    return lista

nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar: ')))

print(
    orden(nombres, True)
)

print(
    orden(nombres, False)
)

#print(
#    orden() #al haber puesto la descripción nos dice en el error que los argumentos que se piden son "lista" y "sentido"