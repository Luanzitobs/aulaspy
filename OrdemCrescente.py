#ORDEM CRESCENTE

lista = []

for i in range (10):

    nome = input("DIGITE SEU NOME : ")
    lista.append(nome)
lista.sort()

print (*lista, sep="\n")

#ORDEM DECRESCENTE

lista = []

for i in range (10):

    nome = input("DIGITE SEU NOME : ")
    lista.append(nome)
lista.sort(reverse=True)

print (*lista, sep="\n")

