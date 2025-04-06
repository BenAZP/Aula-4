N = int(input("Digite os N termos de fibonacci: "))

if N <= 0:
    print("a quantiodade de termos tem que ser maior que zero")
elif N == 1:
    print("0")
else:
    a = 0
    b = 1
    print(a, end=" ")

    if N > 1:
        print(b, end=" ")

    count = 2
    while count < N:
      c = a + b
      print(c, end=" ")
      a = b
      b = c
      count += 1
    
