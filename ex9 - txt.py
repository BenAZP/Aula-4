# Abre o arquivo ex9.txt para escrita
arquivo = open("ex9.txt", "w")

N = int(input("Digite os N termos de fibonacci: "))

if N <= 0:
    mensagem = "a quantiodade de termos tem que ser maior que zero"
    print(mensagem)
    arquivo.write(mensagem + "\n")
elif N == 1:
    print("0")
    arquivo.write("0\n")
else:
    a = 0
    b = 1
    print(a, end=" ")
    arquivo.write(f"{a} ")

    if N > 1:
        print(b, end=" ")
        arquivo.write(f"{b} ")

    count = 2
    while count < N:
        c = a + b
        print(c, end=" ")
        arquivo.write(f"{c} ")
        a = b
        b = c
        count += 1

arquivo.close()
