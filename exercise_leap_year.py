def leap_year():
    año_input = int(input())

    if (año_input % 4 == 0) and (año_input % 100 != 0 or año_input % 400 == 0):
        print(f"El año {año_input} es bisiesto")
    else:
        print(f"El año {año_input} no es bisiesto")

# leap_year()