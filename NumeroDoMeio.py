#Descobrir o número do meio

numeros = []

for i in range (5):
    num = int(input("digite seu numero : "))
    numeros.append(num)

numeros.sort (reverse=True) 

numeroDoMeio = int((len(numeros)-1)/2)

print (f"{numeros}. O numero do meio é {numeros[numeroDoMeio]}")
