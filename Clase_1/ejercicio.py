### Ejercicio 1
a = 2.4
b = -3.21
c = 47.8
print("a\tb\tc\n",a,"\t",b,"\t",c)

####Ejercicio 3
texto = input('Escriba aquí:')
divtexto = texto.split(" ")
for i in divtexto: 
    print(i,(len(i)* "*"))
    
###Ejercicio 4
dictexto = {}
for i in divtexto: 
   dictexto.update(dict([(i,(len(i)* "*"))]))
print(dictexto)
