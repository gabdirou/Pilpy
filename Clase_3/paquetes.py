#Los import siempre van arriba de todo

#import pandas as pd #para cambiarle el nombre el as

#from pandas import DataFrame #para importar solamente una función del framework

#from pandas import DataFrame as df # para cambiar el nombre a la función que se va a importar 

import funciones #Para ver todas las funciones que ya definimos en otros archivos e ir eligiendo
from funciones import saludo #Para traer especificas
from Clase_3.funciones import orden #para traer de una ruta especifica
from funciones import saludo, orden

#Con la carpeta utilidades y poniendo el archivo _init_ le decimos a py que se trata de un paquete. Allí se pueden ubicar todas las
#funciones que usemos


#para que colegas puedan ver que paquetes usamos en la consola hacemos: 
# <pip list> <pip freeze > requirements.txt >, subimos ese archivo al repo.
# Para traer los paquetes de otros colegas:
# <pip install -r requirements.txt> 

