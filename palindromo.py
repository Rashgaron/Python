def inversa(cadena):
	i = len(cadena)-1
	res = ""
	while i >= 0:
		res += cadena[i]
		i -=1

	return res

def palindromo(cadena,Scadena):
	pal = True
	i = 0
	while pal == True and i < len(cadena):
		if cadena[i] != Scadena[i]:
			pal = False
		i +=1
	return pal




def main():



	cadena = input("Introduce una cadena de texto para que sea invertida. ")
	Scadena = inversa(cadena)
	
	if palindromo(cadena,Scadena):
		print("Es palindromo")
	else:
		print("No es palindromo")

main()
