def max_de_tres(a,b,c):

	if a > b and a > c:
		print(a)
	elif b > a and b > c:
		print(b)
	elif c > a and c > b:
		print(c)
	else:
		print("Todos son iguales")

def main():
	max_de_tres(4,7,2)


main()
