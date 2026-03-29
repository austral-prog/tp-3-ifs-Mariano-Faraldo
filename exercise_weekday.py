def weekday():
    Dia_semana = input("Coloque un dia de la semana: ")

    Dia_semana = Dia_semana.lower()

    if "sabado" not in Dia_semana and "domingo" not in Dia_semana:
        print("Dia habil")
    else:
        print("Fin de semana")

# weekday()