n = int (input())

for num in range (n):
    numero = int (input())
    if numero % 2 == 0 and numero > 0:
        print ("EVEN POSITIVE")
    elif numero % 2 != 0 and numero < 0:
        print ("ODD NEGATIVE")
    elif numero % 2 == 0 and numero < 0:
        print ("EVEN NEGATIVE")
    elif numero % 2 != 0 and numero > 0:
        print ("ODD POSITIVE")
    else:
        print ("NULL")
  


   