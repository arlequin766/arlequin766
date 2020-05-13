# Listas
autos = ['Ford', 'Chevrolet', 'Flat']
print(autos)
autos.append('Dodge')
print(autos)
autos.insert(1, 'Ferrari')
print(autos)
del autos[2]
print(autos)
print(len(autos))
autos[2] = 'Porsche'
print(autos)
if autos[2] == 'Porsche':
	print('Todo bien')
else:
	print('Todo mal')


# Tuplas
colores = ('Amarrillo', 'Azul', 'Verde')
print(colores)
# colores[2] = 'rojo' # No se puede cambiar valores en la tupla
print('Amarrillo' in colores)
if 'Amarrillo' in colores:
	print('El amarillo existe')


# Diccionarios
usuario = {'id':1, 'name':'pedro', 'age':37, 'casado':True}
print(usuario)
print(usuario['name'])
usuario['name'] = 'Nacy Tupla'
print(usuario)
usuario['apellido'] = 'Algo'
print(usuario)
del usuario['apellido']
print(usuario)
print(usuario.keys())
print(usuario.values())
if 'id' in usuario:
	print('Tiene ID')
usuario.clear()
print(usuario)
del usuario
print(usuario)




























