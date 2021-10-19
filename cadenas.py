# Ejemplo de cadenas

s1 = "Parte 1"
s2 = "Parte 2"
print(s1 + " " + s2)  #Parte 1 Parte 2

s = "curso de Python"
print(type(s))  #<class 'str'>

#Formateo de cadenas
x = 5
s = "El número es: " + str(x)
print(s) 

s = "Los números son %d y %d." % (5, 10)
print(s) 

#uso de format cadenas
s = "Los números son {} y {}".format(5, 10)
print(s) 

s = "Los números son {a} y {b}".format(a=5, b=10)
print(s)  #Los números son 5 y 10

#cadenas literales o f-strings, permite incrustar expresiones dentro de cadenas.
a = 5; b = 10
s = f"Los números son {a} y {b}"
print(s) #Los números son 5 y 10

#Se puede multiplicar un string por un int. Su resultado es replicarlo tantas veces como el valor del entero.
s = "Hola "
print(s*3) #Hola Hola Hola

#Podemos ver si una cadena esta contenida en otra con in.
print("mola" in "Python mola") #True

#Con chr() and ord() podemos convertir entre carácter y su valor numérico que lo representa y viceversa. El segundo sólo función con caracteres, es decir, un string con un solo elemento.
print(chr(8364)) #€
print(ord("€"))  #110
