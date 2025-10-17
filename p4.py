n1 = float (input())
n2 = float (input())
n3 = float (input())
n4 = float (input())

p1 =  0.3
p2 =  0.3
p3 =  0.2
p4 =  0.2

mediaPond = (n1*p1 + n2*p2 + n3*p3 + n4*p4)/(p1+p2+p3+p4)

if mediaPond >= 7 :
    print ("APROVADO")
elif mediaPond >= 5 and mediaPond <7 :
    print ("RECUPERACAO")
else:
    print ("REPROVADO")