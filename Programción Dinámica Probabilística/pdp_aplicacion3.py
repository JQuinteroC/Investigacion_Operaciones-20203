def funcion_lote(x, funcion_recursiva):
    """Calcula la función funcion_recursiva según X

    Args:
        x (int): variable de desición
        funcion_recursiva (none): función a operar

    Returns:
        int: valor de la funcion funcion_recursiva evaluada en x
    """
    if x == 0:
        return x + funcion_recursiva * (0.5**x)

    return 3 + x + funcion_recursiva * (0.5**x)


def min_valor(funcion_recursiva):
    """Evalua la funcion_recursiva en busqueda del menor valor posible

    Args:
        funcion_recursiva (none): función recursiva de la etapa

    Returns:
        list: menor valor de la función y valor de X
    """
    xn = []

    xn.append(funcion_lote(0, funcion_recursiva))

    # Se pone en dos condiciones para revisar el siguiente y el siguiente a este, pues se puede dar el caso...tal vez se podria optimizar
    while xn[len(xn) - 1] >= funcion_lote(len(xn), funcion_recursiva) or xn[len(xn) - 1] >= funcion_lote(len(xn) + 1, funcion_recursiva):
        xn.append(funcion_lote(len(xn), funcion_recursiva))

    return min(xn), xn.index(min(xn))


def iteracion(numero_iteraciones, valor_inial):
    """Realiza las numero_iteraciones con la función valor_inicial

    Args:
        numero_iteraciones (int): Número de iteraciones a realizar
        valor_inial (float): Valor de la restricción inicial

    Returns:
        List[list]: Una lista de listas con la información del menor valor y valor de X por iteración
    """
    sol_iteracion = []

    sol_iteracion.append(min_valor(valor_inial))

    for i in range(numero_iteraciones - 1):
        sol_iteracion.append(min_valor(sol_iteracion[i][0]))

    sol_iteracion.reverse()

    return sol_iteracion


if __name__ == "__main__":
    # Valores del problema
    numero_iteraciones = 3
    funcion_inial = 16

    solucion = iteracion(numero_iteraciones, funcion_inial)
    print("Para obtener las mayores ganancias se debe invertir:\n\naño 1: Oro\naño 2: Oro\naño 3: Oro\n\nDonde se obtendra una ganancia de 9800 dolares")
