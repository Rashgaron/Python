def anadir_elemento(lista):
	n = int(input("Introduce la cantidad de elementos que quieres anadir a la lista:"))
	i = 0
	while i < n:

		elemento = input()
		lista.append(elemento)
		print("El elemento " +elemento+ " ha sido anaido")
		i +=1
def mostrar_lista(lista):
	print("Mostrando elementos de la lista: ")
	if len(lista) != 0:
		for i in lista:
			print(i)	
	else:
		print("La lista esta vacia")
def main():
	lista=[]
	continua = True
	while continua:
		print("[Mostrar_lista]		[Anadir_elemento]	[Salir]")
		op = input("Introduce la operacion que quieras realizar: ")
		if op =="Mostrar_lista":
			mostrar_lista(lista)
		elif op == "Anadir_elemento":
			anadir_elemento(lista)	
		elif op == "Salir":
			continua = False
try:
	main()
except KeyboardInterrupt:
	print()
	print("Cierre forzado del programa")	
