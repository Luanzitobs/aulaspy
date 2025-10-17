valor  = int(input("Digite um numero:"))
print(valor)
notas = [100,50,20,10,5,2,1]
for nota in notas:
    qt = valor // nota
print(f"{qt} notas(s)de R$ {notas},00")
valor = valor % nota