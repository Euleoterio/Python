arquivo = open("arquivo.txt")

linhas = arquivo.readlines() #le arquivo e salva na variavel linhas

for linha in linhas:
	print(linha)


texto_completo = arquivo.read() 
print(texto_completo)


