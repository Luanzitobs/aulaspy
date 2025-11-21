######################### JUNTAR ######################

def juntar (x , y):
    resposta = x + y 
    return resposta

entrada1 = input("digite algo : ")  #int se quiser somar
entrada2 = input("digite alguma coisa : ")

r = juntar (entrada1 , entrada2)

print (r)

########################### MAIOR VERDADEIRO E FALSO ########################

def maior10 (x):
    if x >10:
        return True
    else:
        return False
for i in range (10):
    valor = int(input("Digite um valor : "))
    print (maior10(valor))
    
    
####################### SOMA E MULTIPLICA ############################

def soma (x , y):
    r = x + y
    return r

def multiplica(a,b):
    res = a * b 
    return res

ent1 = int(input("Digite um valor : "))   
ent2 = int(input("Digite um valor : "))

print (f"A soma é : {soma(ent1 , ent2)}")   
print (f"A multiplicação é : {multiplica(ent1 , ent2)}")   

################################ OUTRA FORMA ###############################
def soma (x , y):
    r = x + y
    return r

def multiplica(a,b,c,d):
    x = soma (a,b)
    y = soma (c,d)
    res = x * y
    return res

r1 = int(input("Digite um valor : "))   
r2 = int(input("Digite um valor : "))
r3 = int(input("Digite um valor : "))
r4 = int(input("Digite um valor : "))

resposta = multiplica(r1,r2,r3,r4)

print (resposta)  
