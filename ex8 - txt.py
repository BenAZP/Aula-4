# Abre o arquivo ex8.txt para escrita
arquivo = open("ex8.txt", "w")

num = int(input("Digite um numero: "))

if num < 2:
    print("Nao e primo")
    arquivo.write("Nao e primo\n")
else:
    i = 2
    cont = 0

    while i < num:
        if num % i == 0:
            cont += 1
        i += 1

    if cont == 0:
        print("É primo")
        arquivo.write("É primo\n")
    else:
        print("Nao e primo")
        arquivo.write("Nao e primo\n")

arquivo.close()
