minha_lista = ["abacaxi","melancia", "abacate"]
lista = [1,2,3]
lista_mista = [1,"abacaxi", 1.1, True]


print(minha_lista)
print(lista)
print(lista_mista)


#por indice
print(minha_lista[1])
print(lista[2])
print(lista_mista[0])

#andar na lista
for item in minha_lista:
	print(item)

#tamanho da lista
tamanho = len(minha_lista)
print(tamanho)

#inserir na lista
minha_lista.append("limao")
print(minha_lista)

#se existe
if 3 in lista:
	print("3 esta na lista")

#remover
del minha_lista [2:] #do 2 ao final
print(minha_lista)

del lista[:] #remove toda lista

#criar em branco
lista_branco = []

lista_branco.append(57) #add
print(lista_branco)


