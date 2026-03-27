def grades():
    nota = int(input())

    if nota > 8 and nota <11:
        print("Excelente")
    elif nota > 6 and nota <9:
        print("Bueno")
    elif nota > 4 and nota <7:
        print("Regular")
    elif nota >= 0 and nota <= 4:
        print("Insuficiente")

grades()

