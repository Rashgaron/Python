from libro import libro

def main():
	biblioteca = {}
	print("introduce los datos del nuevo libro:")
	tipo = 	input("Introduce el tipo: ");
	nombre = input("Introduce el nombre: ")
	isbn = input("Introduce el isbn: ")
	biblioteca [isbn] = libro(tipo,nombre,isbn)
	elemento = input("Introduce el libro que quieres buscar; ")
	a = biblioteca[elemento]
	print(a.tipo,a.nombre,a.isbn)

main()
