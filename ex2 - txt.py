max = int(input("Maximo:"))
min = int(input("Minimo:"))

# Abre o arquivo para escrita
arquivo = open("ex2.txt", "w")

if max > min:
    num = min
    while num <= max:
        if num % 5 == 0:
            print(num)
            arquivo.write(f"{num}\n")
        num += 1
else:
    print("Numero invalido")
    arquivo.write("Numero invalido\n")

arquivo.close()
