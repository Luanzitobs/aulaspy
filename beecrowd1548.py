N = int(input())  
for _ in range(N):
    M = int(input())  
    notas = list(map(int, input().split()))

    ordenadas = []
    for nota in notas:
        ordenadas.append(nota)

    for i in range(M):
        for j in range(0, M - 1):
            if ordenadas[j] < ordenadas[j + 1]:
                temp = ordenadas[j]
                ordenadas[j] = ordenadas[j + 1]
                ordenadas[j + 1] = temp
    sem_troca = 0
    for i in range(M):
        if notas[i] == ordenadas[i]:
            sem_troca += 1

    print(sem_troca)
