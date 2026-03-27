def age_check():
   edad = int(input())

   limite_mayor = int(input())

   if edad <= 0 or limite_mayor <= 0:
    print("Entrada invalida")
   else:
    if edad >= limite_mayor:
        print("Eres mayor de edad")
    elif edad < limite_mayor:
        print("Eres menor de edad")


age_check()


