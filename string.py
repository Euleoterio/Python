a = "Vinicius"
b = "Euleoterio"
minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r")
busca = minha_string.find("rei")


print(busca)
print(minha_lista)
print(minha_string[busca:])

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

concatenar = a + " " + b
print(concatenar)

tamanho = len(concatenar)
print(tamanho)

print(a[0])
print(b[2:8])

print(concatenar.lower())
print(concatenar.upper())

print(a + "\n" + b)
print(concatenar.strip()) # tira espaço se tiver 

print (concatenar.split())