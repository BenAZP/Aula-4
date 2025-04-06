num = int(input("Digite um numero: "))

if num < 2:
     print("Nao e primo")
else:
     i = 2
     cont = 0

     while i < num:
         if num % i == 0:
             cont += 1
         i += 1
             
     if cont == 0:
        print("É primo")
     else:
        print("Nao e primo")
