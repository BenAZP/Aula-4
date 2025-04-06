# Leitura do número N e do valor Prim
N = int(input("Digite os N termos de Fibonacci: "))
Prim = int(input("Digite o valor de Prim: "))

if N <= 0:
    print("A quantidade de termos tem que ser maior que zero")
elif N == 1:
    if 0 > Prim:
        print("0")
else:
    a = 0
    b = 1
    # Verifica se o primeiro termo é maior que Prim
    if a > Prim:
        print(a, end=" ")
    
    # Verifica se o segundo termo é maior que Prim
    if b > Prim:
        print(b, end=" ")
    
    count = 2  # Já imprimimos os dois primeiros termos
    while count < N:
        c = a + b
        if c > Prim:  # Verifica se o termo c é maior que Prim
            print(c, end=" ")
        a = b
        b = c
        count += 1
