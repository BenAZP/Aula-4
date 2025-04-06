numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
else:
    print("Número fora do intervalo permitido.")
