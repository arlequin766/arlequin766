def calcular_precio(marca,puerta,color):
	marcas = {'ford':100000, 'chevrolet':120000, 'flat':800000}
	colores = {'Blanco':10000, 'Azul':20000, 'Negro':30000}
	puertas = {2:50000, 4:65000,5:78000}
	precio = marcas[marca]+colores[color]+puertas[puerta]
	return precio

mas_clietes = 'si'

ventas = []
marcas = ['ford', 'chevrolet', 'flat']
puertas = [2,4,5]
colores = ['Blanco', 'Azul', 'Negro']

while mas_clietes == 'si':
	nombre = raw_input('Ingrese nombre: ')
	apellido = raw_input('Ingrese apellido: ')
	marca = ''
	puerta = 0
	color = ''
	while marca not in marcas:
		marca = raw_input('Ingrese marca: ')
		marca = marca.lower()
	while puerta not in puertas:
		puerta = int(raw_input('Ingrese puertas: '))
	while color not in colores:
		color = raw_input('Ingrese color: ')
	precio = calcular_precio(marca,puerta,color)
	ventas.append({'nombre':nombre, 'apellido':apellido, 'marca':marca, 'puerta':puerta, 'color':color, 'precio':precio})
	mas_clietes = raw_input('Hay mas clietes?: ')

largo = len(ventas)

for i in ventas:
	if largo > 5 and largo < 11:
		i('precio') = i('precio') * 0.9
	if largo > 10 and largo < 51:
		i('precio') = i('precio') * 0.85
	elif largo > 50:
		i('precio') = i('precio') * 0.82

		print('La personal {} {} compro un auto marca {} de {} puertas y color {} con un precio de: {}'.format(nombre, apellido, marca, puerta, color, precio))

