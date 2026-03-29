def triangle():
    numero_1 = float(input())
    numero_2 = float(input())
    numero_3 = float(input())

    if numero_1 + numero_2 > numero_3 and numero_1 + numero_3 > numero_2 and numero_2 + numero_3 > numero_1:
        print("Los lados forman un triangulo valido")

    else:
        print("Los lados no forman un triangulo valido")
        
# triangle()