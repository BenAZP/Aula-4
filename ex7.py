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
    media = soma/qtd
    print(f"\nnumero maior: {maior}")
    print(f"numero menor: {menor}")
    print(f"somatoria: {soma}")
    print(f"quantidade: {qtd}")
    print(f"media: {media}")


else:
    print("Nenhum numero valido inserido")
        
    
