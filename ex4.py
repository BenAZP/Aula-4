N = int(input("Digite a quantidade de numeros a serem listados:"))

if N <= 0:
    print("Quantidade invalida")
else:
    contador = 0
    
    numero = float(input("Digite um numero: "))
    
    while numero <= 0:
         print("Numero invalido")
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
           
    print(f"numero maior: {maior}")
    print(f"numero menor: {menor}")
