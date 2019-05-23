def es_vocal(letra):
	if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra =='E' or letra =='I' or letra == 'O' or letra == 'U':
		return True
	else:
		return False

def main():
	while True:
		letra = input("Introduce un caracter: ")
		
		if es_vocal(letra):
			print("Es vocal")
		else:
			print("Es consonante")
try:
	main()
except KeyboardInterrupt:
	print("Vaya, has acabado el programa")	
