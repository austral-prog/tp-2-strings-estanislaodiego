def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Introduce gasto: "))
    dinero_recibido = int(input("Dinero recibido"))
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = float(vuelto - pesos) * 100

    print("\nVuelto")
    print("\nPesos:")
    print(pesos)
    print("\nCentavos:")
    print(int(centavos))
