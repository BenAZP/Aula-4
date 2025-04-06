N = int(input("Digite a quantidade de numeros a serem listados:"))

# Abre o arquivo para escrita
arquivo = open("ex4.txt", "w")

if N <= 0:
    print("Quantidade invalida")
    arquivo.write("Quantidade invalida\n")
else:
    contador = 0

    numero = float(input("Digite um numero: "))

    while numero <= 0:
        print("Numero invalido")
        arquivo.write("Numero invalido\n")
        numero = float(input("Digite um numero: "))

    maior = menor = numero
    contador += 1

    while contador < N:
        numero = float(input("Digite um numero: "))

        if numero > 0:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

            contador += 1
        else:
            print("Numero invalido")
            arquivo.write("Numero invalido\n")

    print(f"numero maior: {maior}")
    print(f"numero menor: {menor}")
    arquivo.write(f"numero maior: {maior}\n")
    arquivo.write(f"numero menor: {menor}\n")

arquivo.close()
