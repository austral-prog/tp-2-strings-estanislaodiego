def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print(f"Palabra: {palabra}")
    longitud = len(palabra)
    print(f"Longitud: {len(palabra)}")
    primera_letra = (palabra[0])
    print(f"Primera letra: {palabra[0]}")
    ultima_letra = palabra[-1]
    print(f"Ultima letra: {ultima_letra}")
    repetida = (palabra * 3)
    print(f"Repetida: {repetida}")
    decorada = ("***" + palabra + "***")
    print(f"Decorada: {decorada}")
