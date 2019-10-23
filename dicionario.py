dicionario = {"A":"Ameixa","B":"Bola","C":"Cachorro"}

print(dicionario["A"]) #print pela chave

#andar dicionario
for chave in dicionario:
	print(chave+ ":"+ dicionario[chave])


#função itens
for i in dicionario.items():
	print(i)

for i in dicionario.values():
	print(i)	