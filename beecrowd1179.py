listapar = []
listaimpar = []
contpar = 0
contimpar = 0
for i in range(15):
    valor = int(input())
    if valor%2 == 0 and contpar < 5:
        listapar.append(valor)
        contpar += 1
        
        if contpar == 5:
            for j,e in enumerate (listapar):
                print(f"par[{j}] = {e}")

            listapar.clear()
            contpar = 0

    if valor%2 != 0 and contimpar < 5:
        listaimpar.append(valor)
        contimpar += 1

        if contimpar == 5:
            for j,e in enumerate(listaimpar):
                print(f"impar[{j}] = {e}")
            listaimpar.clear()
            contimpar = 0

for i in range(len(listaimpar)):
    print(f"impar[{i}] = {listaimpar[i]}")
            
for i in range(len(listapar)):
    print(f"par[{i}] = {listapar[i]}")
