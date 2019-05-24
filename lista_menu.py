

def anadir_elemento(lista):

	n = int(input("Introduce la cantidad de elementos que quieres anadir a la lista:"))
	i = 0
	while i < n:

		elemento = input()
		lista.append(elemento)
		print("El elemento " +elemento+ " ha sido anaido")
		i +=1
	print()

def mostrar_lista(lista):

	print("Mostrando elementos de la lista: ")
	if len(lista) != 0:
		#for i in lista:
		#	print(i)
		print(lista)	
	else:
		print("La lista esta vacia")
	

def eliminar_elemento(lista):
	j =int(0)
	mostrar_lista(lista)
	existe = False
	n_elem =int( input("Introduce la cantidad de elementos que quieres eliminar: "))
	while j < n_elem:

		n = str(input("Introduce el elemento que quieres eliminar: "))
		for i in lista:
			if i == n:
				print("Vamos a eliminar el elemento " +n+ " de la lista")
				lista.remove(n)
				existe = True
				break 
		if not existe:
			print("El elemento " + n + " no existe dentro de la lista")
		j +=1
	print()

def guardar_datos(lista):

	file = open("lista_elementos.txt","w")
	for i in lista:
		file.write(i+'\n')
	file.close()

def cargar_datos(lista):

	with open("lista_elementos.txt","r") as f:
		for line in f:
			for word in line.split():
				lista.append(word)
	


def main():

	lista=[]	
	cargar_datos(lista)	
	continua = True
	while continua:
		print("[Mostrar_lista]		[Anadir_elemento]	[Eliminar_elemento]	[Salir]")
		print()			
		try:
			op = input("Introduce la operacion que quieras realizar: ").split()[0]
		except IndexError:
			print("No has introducido una opcion valida")
			main()
		if op =="Mostrar_lista":
			mostrar_lista(lista)
		elif op == "Anadir_elemento":
			try:
				anadir_elemento(lista)
			except ValueError:
				print("Has introducido un valor incorrecto")
		elif op == "Eliminar_elemento":
			try:
				eliminar_elemento(lista)
			except ValueError:
				print("Has introducido un valor incorrecto")	
		elif op == "Salir":
			continua = False
	guardar_datos(lista)
try:
	main()
except KeyboardInterrupt:
	print()
	print("Cierre forzado del programa")

