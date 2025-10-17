disntanciaKM = float(input("SUA DISTANCIA EM KM : "))
gasolina = float(input("SUA GASOLINA EM LITROS : "))
distanciaDaViagem =  float(input("DISTANCIA DA PROXIMA VIAGEM EM KM : "))

consumedio = gasolina / disntanciaKM
combustEstimado = consumedio * distanciaDaViagem 

print (f"SEU CONSUMO MEDIO É {consumedio:.2f} Litros de gasolina")
print (f"SUA PROXIMA VIAGEM VAI LEVAR EM MEDIA {combustEstimado:.2f} Litros de gasolina")