def calculator():
    numero_1 = float(input())

    numero_2 = float(input())

    operacion = input()

    if operacion == "+":
        resultado = numero_1 + numero_2
        print(f"Resultado: {resultado}") 
    elif operacion == "-":
        resultado = numero_1 - numero_2
        print(f"Resultado: {resultado}") 
    elif operacion == "*":
        resultado = numero_1 * numero_2
        print(f"Resultado: {resultado}") 
    elif numero_2 == 0:
        print("Error: division por cero")
    elif operacion == "/":
        if numero_2 == 0:
            print("Error: division por cero")
        else:
            resultado = numero_1 / numero_2
            print(f"Resultado: {resultado}") 
    else:
        print("Operacion invalida")
       

calculator()