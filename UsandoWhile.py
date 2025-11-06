#MAXIMO,MINIMO,SOMA,QUANTIDADE,DE UMA LISTA

lista = []
entrada = -1


while entrada != 0:
    
    
    entrada = int(input("digite um numero : "))
    if(entrada!=0):
        lista.append(entrada)
    
print("Maior = ", max(lista))
print("Menor = ", min(lista))
print("Soma = ", sum(lista))
print("Quantidade = ", len(lista))
