# Ejemplo de tuplas

tupla = 1, 2, ('a', 'b'), 3
print(tupla)       
print(tupla[2][0]) 

#también es posible convertir una lista en tupla haciendo uso de al función tuple()
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) 
print(tupla)   

#se puede también asignar el valor de una tupla con n elementos a n variables.
x, y, z = tupla
print(x, y, z) 
