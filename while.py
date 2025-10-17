nome = input ("Digite seu nome : ")
while nome != "":
    nota1 = float(input("Digite sua nota : "))
    nota2 = float(input("Digite sua nota : "))
    nota3 = float(input("Digite sua nota : "))
    media = (nota1 + nota2 + nota3)/3
    print ("Olá ," ,nome,", você teve a media : ", media)
    nome = input("Digite seu nome : ")