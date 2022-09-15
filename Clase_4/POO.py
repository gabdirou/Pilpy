# Clase
#class Perro:
#    pass #para crear cosas sin agregar nada
#en ese caso se puede crear por ej perro:1 = Perro() sin atributos


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self, sonido):
        print(sonido)

class Gato(Animal):

    def __init__(self, nombre, raza, especie, edad):
        self.nombre = nombre 
        self.raza = raza 
        
        super().__init__(especie, edad)

    #Métodos
    def saludar(self):
        print(self.nombre, 'ronronea')


class Perro: #class Perro(Animal): para que herede de animal 
    
    #Atributos de clase == global (serán comunes a todos, se mantienen para todos)
    especie = 'mamíferos'


    def __init__(self, nombre, raza):
        # Atributos de instancia == locales (serán independientes)
        self.nombre = nombre #self.nombre = '' (vació para asignar cosas luego)
        self.raza = raza #self.raza = ''

        #super().__init__(especie,edad) #esto para traer los atributos de la super clase

    def ladrar(self): #self para decir que es acción propia de la clase 
        print('Guau')
    
    def jugar(self, objeto):
        print('El perro está jugando con ', objeto)
    
    #Métodos
    def saludar(self):
        print(self.nombre, 'dio la pata')





#para inicializar el objeto

perro_1 = Perro('Rex','Collie') #Acá le ponemos los parámetros nombre y raza
print(f'Perro_1 --> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}')
print(type(perro_1))
print(perro_1.raza) #para acceder al atributo

perro_2 = Perro('Ana', 'Collie')

perro_1.ladrar()
perro_1.jugar("pelota")
perro_1.saludar()

#perro_3 = Perro() #en caso de que esté vacío para asignar valores
#perro_3.nombre = 'Firulais'
#perro_3.raza = 'Salchicha'

gato_1 = Gato('Tito', 'Calico', 'Felino', 3)
print(gato_1.raza)