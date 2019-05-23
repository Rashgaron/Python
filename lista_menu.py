

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
		for i in lista:
			print(i)	
	else:
		print("La lista esta vacia")
	print()
def eliminar_elemento(lista):
	existe = False
	n = input("Introduce el elemento que quieres eliminar: ")
	for i in lista:
		if i == n:
			print("Vamos a eliminar el elemento " +n+ " de la lista")
			lista.remove(n)
			existe = True 
	if not existe:
		print("El elemento " + n + " no existe dentro de la lista")
	print()
def main():
	lista=[]
	continua = True
	while continua:
		print("[Mostrar_lista]		[Anadir_elemento]	[Eliminar_elemento]	[Salir]")
		print()
		op = input("Introduce la operacion que quieras realizar: ")
		if op =="Mostrar_lista":
			mostrar_lista(lista)
		elif op == "Anadir_elemento":
			anadir_elemento(lista)
		elif op == "Eliminar_elemento":
			eliminar_elemento(lista)	
		elif op == "Salir":
			continua = False
try:
	main()
except KeyboardInterrupt:
	print()
	print("Cierre forzado del programa")	
