mulheres = 0
idade = 0

while True:

    sexo = input ("Digite seu sexo (F , M , O ) :") 
    idade = int (input("Digite sua idade :"))

    if sexo == "F" and idade >= 18:
        mulheres +=1

    if mulheres == 5:
        break 

print (f"Entraram {mulheres} mulheres")
