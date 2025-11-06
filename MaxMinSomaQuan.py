#MAXIMO,MINIMO,SOMA,QUANTIDADE,DE UMA LISTA

lista = []


for i in range (10):
    lista.append(int(input()))
print("Maior = ", max(lista))
print("Menor = ", min(lista))
print("Soma = ", sum(lista))
print("Quantidade = ", len(lista))
