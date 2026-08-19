def filtrar_vocales(cadena, bandera):
    """"
    :param cadena: string
    :param bandera: boolean
    :return: estado: int, cadena_final: string
    """

    # se defina una lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']

    #se define el abcedario
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                  'x', 'y', 'z']

    # se revisa que la variable cadena si sea de tipo string
    if not isinstance(cadena, str):
        return -100, None

    # se revisa que cada letra de la cadena esté en el abecedario
    for letra in cadena:
        if letra.lower() not in abecedario:
            return -200, None

    # se revisa que la cadena no esté vacía
    if cadena == '':
        return -300, None

    # se revisa que la longitud de la cadena sea menor a 30
    if len(cadena) > 30:
        return -400, None

    # se revisa que la bandera sea tipo booleano
    if not isinstance(bandera, bool):
        return -500, None

    cadena_final = ''

    # se itera por la cadena de strings, y dependiendo del flag,
    # se guardan las vocales o las consonantes
    for letra in cadena:
        if bandera:
            if letra.lower() in vocales:
                cadena_final += letra
        else:
            if letra.lower() not in vocales:
                cadena_final += letra

    return 0, cadena_final


def encontrar_extremos(lista_numeros):
    """"
    :param lista_numeros: list
    :return: estado: int, numero_minimo: int o float, numero_maximo: int o float
    """

    # se revisa que la variable lista_numeros si sea de tipo list
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # se revisa que cada elemento en la lista sea tipo int o float
    for numero in lista_numeros:
        if isinstance(numero, bool):
            return -700, None, None

        if (not isinstance(numero, float)) and (not isinstance(numero, int)):
            return -700, None, None

    # se revisa que la lista no esté vacía
    if lista_numeros == []:
        return -800, None, None

    # se revisa que la longitud de la lista sea menor a 15
    if len(lista_numeros) > 15:
        return -900, None, None

    # se busca el mínimo y el máximo en la lista de números
    numero_maximo = max(lista_numeros)
    numero_minimo = min(lista_numeros)

    return 0, numero_minimo, numero_maximo

# pytest tarea_1_testing.py
