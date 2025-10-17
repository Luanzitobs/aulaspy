n1 = float (input("PRIMEIRA NOTA : "))
n2 = float (input("SEGUNDA NOTA : "))
n3 = float (input("TERCEIRA NOTA : "))

peso1 = 0.3
peso2 = 0.5 
peso3 = 0.2

media = (n1 + n2 + n3)/3
mediaPonderada = (n1*peso1 + n2*peso2 + n3*peso3)/(peso1+peso2+peso3)

print (f"SUA MEDIA É : , {media:.2f}")
print (f"SUA MEDIA PONDERADA É : {mediaPonderada:.2f}")