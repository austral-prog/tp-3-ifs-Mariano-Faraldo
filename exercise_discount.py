def discount():
    precio_producto = float(input())

    cantidad_unidades = int(input())

    precio_final_1 = precio_producto * cantidad_unidades

    if cantidad_unidades >= 10:
        descuento = 0.20

        descuento_aplicado = precio_final_1 * (1 - descuento)

        porcentaje_descuento = "20%"

    elif cantidad_unidades >= 5 and cantidad_unidades <= 10:
        descuento = 0.10

        descuento_aplicado = precio_final_1 * (1 - descuento)

        porcentaje_descuento = "10%"

    elif cantidad_unidades < 5:
        descuento = 0
        porcentaje_descuento = "0%"

    monto_descuento = precio_final_1 * descuento
    total_final = precio_final_1 - monto_descuento

    print(f"Subtotal: {precio_final_1}")
    print(f"Descuento aplicado: {porcentaje_descuento}")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total_final}")

discount()

    
