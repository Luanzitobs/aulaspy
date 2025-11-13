print("")

alunos = []

for i in range (2):
    nome = input("Digite o nome do aluno : ") 
    print("")   
    matricula = input("Digite a matricula do aluno : ")  
    print("")  
    cpf = input("digite o CPF do aluno : ")
    print("")    
    nota1 = float(input("Digite sua primeira nota : "))   
    print("") 
    nota2 = float(input("Digite sua segunda nota : "))    
    print("")
    nota3 = float(input("Digite sua terceira nota : "))   
    print("") 
    nota4 = float(input("Digite sua quarta nota : "))   
    print("") 
    dicionario = {"nome": nome, "matricula": matricula, "cpf": cpf, "nota1": nota1, "nota2": nota2, "nota3": nota3, "nota4": nota4 }
    alunos.append(dicionario)
    
#IMPRIME TODAS AS INFORMACOES DOS ALUNOS
print("INFORMACOES DE TODOS OS ALUNOS")
for aluno in alunos:
     print(aluno)
     
#APENAS ALUNOS QUE TIRARAM NOTA > 70 NA NOTA2
print("ALUNOS COM SEGUNDA NOTA ACIMA DE 70:")
for aluno in alunos:
    if (aluno["nota2"] > 70):
         print (aluno["nome"])
        
#NONE DO ALUNO + SUA MEDIA FINAL
print("NOME DOS ALUNOS E SUAS MEDIAS :")
for aluno in alunos:
    media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"] + aluno["nota4"])/4
    print(f"{aluno["nome"]} / MEDIA = {media:.2f}")
