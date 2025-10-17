n = int(input())
i = 0
out = 0 

for k in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        i += 1
    else:
        out +=1 
    
print (f"{i} in")
print (f"{out} out")
    