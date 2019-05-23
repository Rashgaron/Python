def largo_cadena(lista):
	cont = 0
	for i in lista:
		cont +=1
	return cont


def main():
	array = [1,5,4,2,3,6,4,2,7,8,2,2,1,0]
	print(largo_cadena(array))

main()
