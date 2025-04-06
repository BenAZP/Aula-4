# Abre o arquivo ex7.txt para escrita
arquivo = open("ex7.txt", "w")

num = int(input("Digite um numero: "))
soma = 0
qtd = 0
maior = menor = num

while num > 0:
    soma += num
    qtd += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    num = int(input("Digite um numero: "))

if qtd > 0:
    media = soma / qtd

    print(f"\nnumero maior: {maior}")
    print(f"numero menor: {menor}")
    print(f"somatoria: {soma}")
    print(f"quantidade: {qtd}")
    print(f"media: {media}")

    arquivo.write(f"numero maior: {maior}\n")
    arquivo.write(f"numero menor: {menor}\n")
    arquivo.write(f"somatoria: {soma}\n")
    arquivo.write(f"quantidade: {qtd}\n")
    arquivo.write(f"media: {media}\n")

else:
    print("Nenhum numero valido inserido")
    arquivo.write("Nenhum numero valido inserido\n")

arquivo.close()
