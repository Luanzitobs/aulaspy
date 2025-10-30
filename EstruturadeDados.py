#Estruturas de dados

lista1 =  [6, 8 , 12 , 1 ,  4 , 5 , 0 , 10]
          #0, 1 , 2 , 3 ,  4 ,  5 , 6 ,  7 POSIÇÕES DA LISTA
          #-8, -7, -6, -5, -4, -3 , -2, -1 POSIÇÕES DA LISTA VOLTANDO
print (lista1[0])  

#EXEMPLO 
nomeDeFest = []

for i in range (5):
    nome = input ("Digite seu nome : ")
    nomeDeFest.append(nome) #.append() adicionar a lista 
    
nomeDeFest.sort() #.sort() ordenar os itens da lista em ordem

print (nomeDeFest) 
