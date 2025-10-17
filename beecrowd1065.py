pares = 0

for i in range (5):
    numeros = int (input())
    if numeros % 2 == 0:
        pares = pares + 1 

print (f"{pares} valores pares")