max = int(input("Maximo:"))
min = int(input("Minimo:"))

if max > min:
  num = min
  while num <= max:
      if num % 5 == 0:
         print(num)
      num += 1
        
else:
    print("Numero invalido")
