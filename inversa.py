def inversa(cadena):
	i = len(cadena)-1
	res = ""
	while i >= 0:
		res +=cadena[i]
		i-=1;


	print(res)


def main():
	cadena = input("Introduce una cadena de texto para que sea invertida: ")
	inversa(cadena)

main()
