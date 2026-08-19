def filtrar_vocales(cadena, bandera):
    vocales = ['a', 'e', 'i', 'o', 'u']
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                  'x', 'y', 'z']

    if not isinstance(cadena, str):
        return -100, None

    for letra in cadena:
        if letra.lower() not in abecedario:
            return -200, None

    if cadena == '':
        return -300, None

    if len(cadena) > 30:
        return -400, None

    if not isinstance(bandera, bool):
        return -500, None

    cadena_final = ''

    for letra in cadena:
        if bandera:
            if letra.lower() in vocales:
                cadena_final += letra
        else:
            if letra.lower() not in vocales:
                cadena_final += letra

    return 0, cadena_final


def encontrar_extremos(lista_numeros):

    if not isinstance(lista_numeros, list):
        return -600, None, None

    for numero in lista_numeros:
        if isinstance(numero, bool):
            return -700, None, None

        if (not isinstance(numero, float)) and (not isinstance(numero, int)):
            return -700, None, None

    if lista_numeros == []:
        return -800, None, None

    if len(lista_numeros) > 15:
        return -900, None, None

    numero_maximo = max(lista_numeros)
    numero_minimo = min(lista_numeros)

    return 0, numero_minimo, numero_maximo

# pytest tarea_1_testing.py
