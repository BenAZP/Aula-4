# Abre o arquivo ex10.txt para escrita
arquivo = open("ex10.txt", "w")

# Leitura do número N e do valor Prim
N = int(input("Digite os N termos de Fibonacci: "))
Prim = int(input("Digite o valor de Prim: "))

if N <= 0:
    mensagem = "A quantidade de termos tem que ser maior que zero"
    print(mensagem)
    arquivo.write(mensagem + "\n")
elif N == 1:
    if 0 > Prim:
        print("0")
        arquivo.write("0 ")
else:
    a = 0
    b = 1
    # Verifica se o primeiro termo é maior que Prim
    if a > Prim:
        print(a, end=" ")
        arquivo.write(f"{a} ")
    
    # Verifica se o segundo termo é maior que Prim
    if b > Prim:
        print(b, end=" ")
        arquivo.write(f"{b} ")
    
    count = 2  # Já analisamos os dois primeiros termos
    while count < N:
        c = a + b
        if c > Prim:  # Verifica se o termo c é maior que Prim
            print(c, end=" ")
            arquivo.write(f"{c} ")
        a = b
        b = c
        count += 1

arquivo.close()
 
