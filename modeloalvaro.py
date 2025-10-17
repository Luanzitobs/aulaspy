quantidade = 0

while quantidade < 5:
    sexo = input ("Digite seu sexo (F , M , O ) :") 
    idade = int (input("Digite sua idade :"))
    if sexo == "F" and idade >= 18:
        quantidade +=1