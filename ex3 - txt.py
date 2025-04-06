N = int(input("Digite a quantidade de numeros a serem listados:"))

# Abre o arquivo para escrita
arquivo = open("ex3.txt", "w")

if N <= 0:
    print("Quantidade invalida")
    arquivo.write("Quantidade invalida\n")
else:
    contador = 1
    numero = float(input("Digite um numero: "))
    maior = menor = numero

    while contador < N:
        numero = float(input("Digite um numero: "))

        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

        contador += 1

    print(f"numero maior: {maior}")
    print(f"numero menor: {menor}")
    arquivo.write(f"numero maior: {maior}\n")
    arquivo.write(f"numero menor: {menor}\n")

arquivo.close()
