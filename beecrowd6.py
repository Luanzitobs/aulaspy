#QUESTAO 1010

peca1, npeca1, vpeca1 = input().split()
peca1= int(peca1)
npeca1= int(npeca1)
vpeca1= float(vpeca1)

peca2, npeca2, vpeca2 = input().split()
peca2 = int(peca2)
npeca2 = int(npeca2)
vpeca2= float(vpeca2)

valorTotal = (npeca1*vpeca1)+(npeca2*vpeca2)

print (f"VALOR A PAGAR: R$ {valorTotal:.2f}")