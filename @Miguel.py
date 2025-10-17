import time
minutos = (int(input()))
segundo = minutos * 60

for num in range (segundo, -1 , -1):
    print (f"Faltam {num} segundos")
    time.sleep(1)