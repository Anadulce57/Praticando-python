def potencia (base, expoente):
    if expoente == 0:
        return 1
    
    else:
        return base * potencia(base, expoente-1)

b = int(input("Qual é a base? "))
e = int(input("Qual é o expoente? "))

if e >= 0:
    print(potencia(b, e))
else: 
    print("Não colocou um expoente válido, deve ser maior ou igual á zero")