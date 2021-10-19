# Ejemplo de diccionarios

persona = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}
print(persona)
print(persona['Nombre'])  
print(persona.get('Nombre')) 

#Si el key al que accedemos no existe, se añade automáticamente.
persona['Direccion'] = "Calle 123"
print(persona)

#otra forma de definir
d2 = dict([
      ('Nombre', 'Pedro'),
      ('Edad', 32),
      ('Documento', 1003486),
])
print(d2)
