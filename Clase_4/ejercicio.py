import random

class Personaje:
   
    def __init__(self, nombre, reino):
        self.nombre = nombre
        self.reino = reino
        self.salud = 500
        self.energia = 450
        self.oro = 50
        self.ataquemin = 0
        self.ataquemax = 50
    
    def salud(self):
        print(f'{self.nombre} tiene {self.salud} puntos de salud')
     
   

class goblin(Personaje):
    def __init__(self, nombre, reino):
        super().__init__(nombre, reino)
        self.raza = "goblin"
        self.clase = "ladrón"
        self.arma = "daga"
        self.salud -= 100
        self.oro_robado = 0
        self.energia += 100
        
    def robar(self): #Para robar a viajeros
        self.oro_robado += 10 
        self.oro += self.oro_robado
        print(f'{self.nombre} robó {self.oro_robado} a viajeros desprevenidos\n {self.nombre} tiene {self.oro} de oro')
    
    def puñalada(self, humano): #Atacar con puñalada
        danio = random.randint(self.ataquemin, self.ataquemax-41)
        humano.salud = humano.salud - danio
        self.energia -= 10
        if danio == 0: # ataque esquivado
            print(f'{humano.nombre} ha esquivado el ataque de {self.nombre}.\n La energia restante de {self.nombre} es {self.energia}')
        else: #ataque realizado
            print(f'{humano.nombre} ha recibido una puñalada, causando {danio} puntos de daño.\n La salud restante de {humano.nombre} es {humano.salud}. \n La energia restante de {self.nombre} es {self.energia}')
    
    def arrojar_daga(self,humano): #para arrojar dagas
        if self.energia < 15 and self.energia >= 10: # si no hay energía suficiente
            print(f'{self.nombre} Intenta arrojar dagas pero está muy cansado \n ¡{self.nombre} da una puñalada!')
            self.puñalada(humano)
        elif self.energia < 10: # no existe energía para realizar ningún ataque
            print(f'{self.nombre} no tiene energía')
            pass
        else: #energía suficiente
            danio = random.randint(self.ataquemin, self.ataquemax-36)
            humano.salud = humano.salud - danio
            self.energia -= 15
            if danio == 0: #ataque esquivado
                print(f'{humano.nombre} ha esquivado el ataque de {self.nombre}.\n La energia restante de {self.nombre} es {self.energia}')
            else: #ataque realizado
                print(f'{humano.nombre} ha sido atacado con dagas arrojadizas recibiendo {danio} puntos de daño.\n La salud restante de {humano.nombre} es {humano.salud}. \n La energia restante de {self.nombre} es {self.energia}')
    
    def golpe_critico(self,humano): # atacar con golpe crítico
        if self.energia < 40 and self.energia >= 10: # si la energía es insuficiente
            print(f'{self.nombre} Intenta hacer un golpe crítico pero está muy cansado')
            ataque_random = random.randint(1,2) #seleccionar al azar otro tipo de ataque
            if ataque_random == 1:
                self.puñalada(humano)
            elif ataque_random == 2:
                if self.energia >= 15: # si la energía es suficiente para este ataque
                    self.arrojar_daga(humano)
                else: #si es insuficiente
                    self.puñalada(humano)
        elif self.energia < 10: #si no hay energía para ningún ataque
            print(f'{self.nombre} no tiene energía')
            pass
        else: #energía suficiente
            danio = random.randint(self.ataquemin, self.ataquemax+1)
            humano.salud = humano.salud - danio
            self.energia -= 40
            if danio == 0: #ataque esquivado
                print(f'{humano.nombre} ha esquivado el ataque de {self.nombre}.\n La energia restante de {self.nombre} es {self.energia}')
            else: #ataque realizado
                print(f'{humano.nombre} ha sido atacado con un golpe crítico, su salud se ve reducida en {danio} puntos.\n La salud restante de {humano.nombre} es {humano.salud}. \n La energia restante de {self.nombre} es {self.energia}')
    
    def ataque_random(self,humano): #ataque random
        ataque_random = random.randint(1,3)
        if ataque_random == 1:
            if self.energia < 10:
                pass
            else:
                self.puñalada(humano)
        elif ataque_random == 2:
                self.arrojar_daga(humano)
        elif ataque_random == 3:
                self.golpe_critico(humano)
                    

class humano(Personaje):
    
    def __init__(self, nombre, reino):
        super().__init__(nombre, reino)
        self.clase = "Espadachín"
        self.raza = "humano"
        self.arma = "espada de madera"
        self.salud += 100
        self.ataquemin = -10
        self.ataquemax = 51
        
    def estocada(self,goblin): #atacar con estocada
        danio = random.randint(self.ataquemin, self.ataquemax-41)
        goblin.salud = goblin.salud - danio
        self.energia -= 10
        if danio <= 0 : #ataque esquivado
            print(f'{goblin.nombre} ha esquivado el ataque de {self.nombre}.\n La energia restante de {self.nombre} es {self.energia}')
        else: #ataque realizado
            print(f'{goblin.nombre} ha recibido una estocada, provocando {danio} puntos de daño.\n La salud restante de {goblin.nombre} es {goblin.salud}.\n La energia restante de {self.nombre} es {self.energia}')
    
    def golpe_poderoso(self, goblin): #ataque golpe poderoso
        if self.energia < 15 and self.energia > 10: #si la energía es insuficiente
            print(f'{self.nombre} Intenta hacer un golpe poderoso pero está muy cansado \n ¡{self.nombre} da una estocada!')
            self.estocada(goblin)
        elif self.energia < 10: # si es insuficiente para cualquier ataque
            print(f'{self.nombre} no tiene energía')
            pass            
        else: #energía suficiente
            danio = random.randint(self.ataquemin, self.ataquemax-35)
            goblin.salud = goblin.salud - danio
            self.energia -= 15
            if danio <= 0 : #ataque esquivado
                print(f'{goblin.nombre} ha esquivado el ataque de {self.nombre}.\n La energia restante de {self.nombre} es {self.energia}')
            else: #ataque realizado
                print(f'{goblin.nombre} ha recibido un golpe poderoso que disminuye su salud en {danio} puntos.\n La salud restante de {goblin.nombre} es {goblin.salud}.\n La energia restante de {self.nombre} es {self.energia} ')
        
    def torbellino_espadas(self,goblin): #atacar con torbellino de espadas
        if self.energia < 40 and self.energia >= 10: #energía insuficiente
            print(f'{self.nombre} Intenta hacer un torbellino de espadas pero está muy cansado')
            ataque_random = random.randint(1,2) #ataque random con menor energía
            if ataque_random == 1:
                self.estocada(goblin)
            elif ataque_random == 2:
                if self.energia >= 15: # si la energía es suficiente para el golpe poderoso
                    self.golpe_poderoso(goblin)
                else: # si es insuficiente
                    self.estocada(goblin) 
        elif self.energia < 10: # la energía no alcanza para ningún ataque
            print(f'{self.nombre} no tiene energía')
            pass
        else: #energía suficiente
            danio = random.randint(self.ataquemin, self.ataquemax+1)
            goblin.salud = goblin.salud - danio
            self.energia -= 40
            if danio <= 0 : #ataque esquivado
                print(f'{goblin.nombre} ha esquivado el ataque de {self.nombre}.\n La energia restante de {self.nombre} es {self.energia}')
            else: #ataque realizado
                print(f'{goblin.nombre} no vio venir el torbellino de espadas, ha recibido {danio} puntos de daño.\n La salud restante de {goblin.nombre} es {goblin.salud}.\n La energia restante de {self.nombre} es {self.energia}')
    
    def ataque_random(self,goblin): #ataque random
        ataque_random = random.randint(1,3)
        if ataque_random == 1:
            if self.energia < 10:
                pass
            else:
                self.estocada(goblin)
        elif ataque_random == 2:
                self.golpe_poderoso(goblin)
        elif ataque_random == 3:
                self.torbellino_espadas(goblin)
            


nombre = input('introduzca su nombre: ').lower()
reino = input('¿De qué reino provienes?: ')
personaje = input('seleccione su personaje, Goblin / Humano: ').lower()
print(personaje)

class_dict = {'goblin' : goblin, 'humano' : humano} # para seleccionar entre Goblin y Humano
 
jugador_1 = class_dict[personaje](nombre, reino) #para asignar la selección a jugador 1

class_dict.pop(personaje) #para quitar la opción de la lista
randomvalues = random.choice(list(class_dict)) #para asignar opción restante a jugador 2 (la idea era incorporar más personajes)
jugador_2 = class_dict[randomvalues]("pedro", "tierra") 


print(f'Bienvenido {jugador_1.nombre}, de la raza {jugador_1.raza} y clase {jugador_1.clase} del reino {jugador_1.reino}')
print(f'Tu oponente es {jugador_2.nombre}, de la raza {jugador_2.raza} y clase {jugador_2.clase} del reino {jugador_2.reino}')
print('¡El combate ha comenzado!')

while True:
    if jugador_2.salud <= 0:
        print("¡Has derrotado a tu oponente!")
        break
    if jugador_2.energia < 10:
        print(f'{jugador_2.nombre} está muy cansado para continuar ¡Has ganado!')
        break
    if jugador_1.energia < 10:
        print('Estas muy cansado para continuar ¡Has perdido!')
        break
    if jugador_1.salud <= 0:
        print('¡Tu oponente te ha vencido!')
        break
    try:
        if jugador_1.raza == "goblin":
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('¿Cómo desea continuar?')
            print(" 1: Robar \n 2: Puñalada \n 3: Arrojar daga \n 4: Golpe Crítico")
            opcion = int(input("¿Qué deseas hacer? "))
            if opcion == 1:
                jugador_1.robar()
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                jugador_2.ataque_random(jugador_1)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            elif opcion == 2:
                jugador_1.puñalada(jugador_2)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                jugador_2.ataque_random(jugador_1)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            elif opcion == 3:
                jugador_1.arrojar_daga(jugador_2)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                jugador_2.ataque_random(jugador_1)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            elif opcion == 4:
                jugador_1.golpe_critico(jugador_2)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                jugador_2.ataque_random(jugador_1)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            else:
                print("Por favor, ingrese una opción válida")
        elif jugador_1.raza == "humano":
                print('¿Cómo desea continuar?')
                print("1: Estocada \n 2: Golpe poderoso \n 3: Torbellino de espadas")
                opcion = int(input('Introduzca su opción: '))
                if opcion == 1:
                    jugador_1.estocada(jugador_2)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    jugador_2.ataque_random(jugador_1)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                elif opcion == 2:
                    jugador_1.golpe_poderoso(jugador_2)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    jugador_2.ataque_random(jugador_1)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                elif opcion == 3:
                    jugador_1.torbellino_espadas(jugador_2)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    jugador_2.ataque_random(jugador_1)
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                else: 
                    print('Por favor, ingrese una opción válida')
    except:
        print('No puedes realizar esa acción')
        

