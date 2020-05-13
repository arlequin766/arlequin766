for i in range(5):
	precio = 0
	nombre = raw_input('Ingrese nombre del comprador: ')
	apellido = raw_input('Ingrese apellido del comprador: ')
	marca = raw_input('Ingrese la marca: ')
	if marca == 'Ford':
		precio = precio + 100000
	elif marca == 'Chevrolet':
		precio = precio + 120000
	elif marca == 'Flat':
		precio = precio + 80000
	puertas = raw_input('Ingrese cantidad de puertas: ')
	if puertas == '2':
		precio = precio + 50000
	elif puertas == '4':
		precio = precio + 65000
	elif puertas == '5':
		precio = precio + 78000
	color = raw_input('Ingrese Color: ')
	if color == 'Blanco':
		precio = precio + 10000
	elif color == 'Azul':
		precio = precio + 20000
	elif color == 'Negro':
		precio = precio + 30000
	print('La personal {} {} compro un auto marca {} de {} puertas y color {} con un precio de: {}'.format(nombre, apellido, marca, puertas, color, precio))
