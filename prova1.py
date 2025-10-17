   ##########PROVA1
dist = float (input())
resp = dist/12
print (resp)

###########

turno = input()
if turno == "M":
    print ("bom dia")
elif turno == "V":
    print("Boa tarde")
elif turno == "N":
    print ("Boa noite")
else:
    print ("Valor Invalidos")

############################

ativ = float(input())
prova = float(input())
resp = ativ * 0.2 + prova * 0.8
print (resp)

#######################

consumo = float(input())
tipo = input()
if tipo == "R" :
    if consumo <= 500:
        print (consumo * 0.4)
    else:
        print (consumo * 0.65)
elif tipo == "C":
    if consumo <= 1000:
        print (consumo * 0.6)
    else:
        print (consumo * 0.7)
else :
    if consumo <= 5000:
        print (consumo * 0.5 )
    else: 
        print (consumo * 0.6)