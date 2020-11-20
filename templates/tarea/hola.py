choices = [1,2,3]
def converter(choices):
	lista = []
	for x in range (0, len(choices)):
		this = [str(x),str(choices[x])]
		lista.append(tuple(this))
	return tuple(lista)
print(converter(choices))