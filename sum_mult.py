def mult(lista):
	res = 1;
	for i in lista:
		res = res*i
	return res
def suma(lista):
	res = 0
	for i in lista:
		res +=i
	return res

def main():
	lista = []
	n = int(input())

	while n != 0:
		lista.append(n)
		n = int(input())

	print("la multiplicacion de los elementos de la lista es: ")
	print(mult(lista))
	print("La suma de los elementos de la lista es: ")
	print(suma(lista))


main()
