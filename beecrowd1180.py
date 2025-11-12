vetor = int(input())
numeros = list(map(int, input().split()))

menornumero = min(numeros)
posicaomenor = numeros.index(menornumero)

print (f"Menor valor: {menornumero}")

print (f"Posicao: {posicaomenor}")
