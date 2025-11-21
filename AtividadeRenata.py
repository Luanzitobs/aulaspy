#1.
def produto (x , y):
    resp = x * y
    return resp


entrada1 = int(input("Digite um valor : "))
entrada2 = int(input("Digite um valor : "))


mult = produto (entrada1 , entrada2)


print (f"O PRODUTO É : {mult}")    
#2.
def maior (x , y):
    if x > y:
        return x
    else:
        return y
   
valor1 = int(input("Digite um valor : "))
valor2 = int(input("Digite um valor : "))


valorMaior = maior(valor1 , valor2)


print(f"O maior é : {valorMaior}")


#3.
def vogal (x):
    if x == "a" or x =="e" or x =="i" or x =="o" or x =="u":
        return "Vogal"
    else:
        return "Consoante"
   
letra = input("Digite uma letra: ")


descobrir = vogal(letra)
print (descobrir)  

#4.
def lista_media(x):
    soma = sum(x)
    quantidade = len(x)
    media = soma / quantidade
    return media


lista = [15, 30, 15]


resultado = lista_media(lista)


print (f"A media da lista é : {resultado}")

#5.
def maior_lista (x):
    maior = x[0]
   
    for numeros in x:
        if numeros > maior:
            maior = numeros
           
    return maior




lista = []


for i in range (3):
    valor = (int(input("Digite um valor : ")))
    lista.append(valor)
   
mai = maior_lista(lista)


print (f"O maior da lista é {mai}")

#6.
def fatorial_numero (x):
    resultado = 1
    for i in range (1, x + 1):
        resultado *= i
    return resultado


numero = int(input("Digite um valor : "))
print (f"O fatorial é : {fatorial_numero(numero)}")

#7.
def fibo (x):
    sequencia = []
   
    a , b = 0 , 1
   
    for i in range (x):
        sequencia.append(a)
        a , b = b, a + b
       
    return sequencia


numero = int (input("Digite um valor : "))
print (fibo(numero))

#8.
def primo (x):
    if x < 2:
        return False
   
    for i in range (2, int (x**0.5)+1):
        if x % i == 0 :
            return False
       
    return True


numeros = int (input("Digite o valor : "))
print (primo(numeros))  
