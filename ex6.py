N = int(input("Digite um numero para soma(minimo 100): "))

while N < 100:
    print("Numero invalido")
    N = int(input("Digite um numero para soma(minimo 100): "))

soma_pares = 0
num = 2

while num <= N:
    soma_pares += num
    num += 2

print(f"\nA soma dos numeros de 1 a {N} é: {soma_pares}")
