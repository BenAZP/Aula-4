numero = int(input("Digite um número de 1 a 10: "))

# Abre o arquivo fora do if para usá-lo dentro depois
arquivo = open("ex1.txt", "w")

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    arquivo.write(f"Tabuada do {numero}:\n")

    i = 1
    while i <= 10:
        linha = f"{numero} x {i} = {numero * i}"
        print(linha)
        arquivo.write(linha + "\n")
        i += 1
else:
    print("Número fora do intervalo permitido.")
    arquivo.write("Número fora do intervalo permitido.\n")

arquivo.close()
  
