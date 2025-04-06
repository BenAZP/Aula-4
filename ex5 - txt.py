arquivo = open("ex5.txt", "w")

num = float(input("Digite um numero: "))

while num != 0:
    if num % 2 == 0 and num % 3 == 0:
        mensagem = f"{num} é divisivel por 2 e 3"
        print(mensagem)
        arquivo.write(mensagem + "\n")

    num = float(input("Digite um numero: "))

arquivo.close()
