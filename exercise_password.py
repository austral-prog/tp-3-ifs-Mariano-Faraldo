def password():
    contra = input()

    muy_corta = len(contra) < 8

    tiene_numero = False
    for digito in "0123456789":
        if digito in contra:
            tiene_numero = True
            break

    if muy_corta:
        print("Contraseña muy corta")
    if not tiene_numero:
        print("Debe contener un numero")

    if not muy_corta and tiene_numero:
        print("Contraseña valida")

password()