def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("ingresar nombre")
    apellido = input("ingresar apellido")
    nombre_y_apellido = (nombre + " " + apellido)

    print (nombre_y_apellido. lower())
    print (nombre_y_apellido. title())
    print (nombre_y_apellido. upper())
    print ("\t" + nombre_y_apellido. lower())
