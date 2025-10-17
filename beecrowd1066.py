pares = 0
impares = 0
positivos = 0
negativos = 0

for num in range (5):
    numeros = int (input())
    if numeros  % 2 == 0:
        pares = pares + 1 
    if numeros % 2 != 0:
        impares = impares + 1
    if numeros > 0:
        positivos = positivos + 1 
    if numeros < 0:
        negativos = negativos + 1

print (f"{pares} valor(es) par(es)")
print (f"{impares} valor(es) impar(es)")
print (f"{positivos} valor(es) positivo(s)")
print (f"{negativos} valor(es) negativo(s)")