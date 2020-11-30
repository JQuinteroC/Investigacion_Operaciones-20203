memo = {}

def obtener_posiciones(lista, valor):
    """Obtiene todas las posiciones correspondientes a un valor dado

    Args:
        lista (List): Lista donde se buscaran las posiciones que sean igual al valor
        valor (none): valor a buscar en la lista

    Returns:
        [List]: Todas las posiciones de ocurrencia del valor en la lista
    """
    posiciones = []
    inicio = 0
    
    while inicio <= len(lista):
        try:
            if lista.index(valor, inicio) in posiciones:
                break
            posiciones += [lista.index(valor, inicio)]
            inicio = lista.index(valor, inicio) + 1
        except:
            return posiciones
    return posiciones


def f(n, s, x = 0, memo = {}, calcular_todo = False):
    """Calcula y genera todos los valores de las tablas de probabilidades

    Args:
        n (int): Etapa de la jugada
        s (int): Fichas disponibles para comenzar la etapa n
        x (int, optional): Fichas a apostar. Defaults to 0
        memo (dict, optional): Guarda los calculos de cada una de las etapas, para calcularlas 1 vez. Defaults to {}.
        calcular_todo (bool, optional): Define si es necesario calcular todas las fichas disponibles (s) para la etapa ingresada (n). Defaults to False.

    Returns:
        [List]: retorna el maximo valor por N de acuedo a la cantidad de S y la cantdad X
    """
    if n == 4:
        if s + x >= 5:
            return 1, 0
        return 0, 0, s
    elif n > 1:
        if s + x >= 5:
            return 1, 0, s

    try:
        return max(memo[abs(n-3)][s+x]), obtener_posiciones(memo[abs(n-3)][s], max(memo[abs(n-3)][s])), s
    except:
        # Determinar si calcula toda la tabla
        if calcular_todo: 
            r = 5
        else:
            r = s+1

        memo[abs(n-3)] = {}
        for j in range(r):
            resultado = []
            for i in range(5):
                if i <= j:
                    resultado += [(1/3) * f(n + 1, j, -i, memo, True)[0] + (2/3) * f(n + 1, j, i, memo)[0]]
            memo[abs(n-3)][j] = resultado
        
        return max(memo[abs(n-3)][s]), obtener_posiciones(memo[abs(n-3)][s], max(memo[abs(n-3)][s])), s


if __name__ == "__main__":
    cantidad_fichas = 0
    
    for i in range(3):
        if i == 0:
            print(
            f'En la ronda {i+1} debe apostar {f(i+1, 3, memo = memo)[1]} fichas para obtener una posibilidad de {round(f(i+1, 3, memo = memo)[0]*100, 2)} % de ganar la apuesta')
            cantidad_fichas = f(i+1, 3, memo = memo)[2]
        else: # Despues de la primer ronda
            print("Si falla y :")
            for j in range(len(memo[i])):
                if f(i+1, j, memo = memo)[0] != 0:
                    print(f'tiene {j} fichas, entonces en la ronda {i+1} debe apostar {f(i+1, j, memo = memo)[1]} fichas para obtener una posibilidad de {round(f(i+1, j, memo = memo)[0]*100, 2)} % de ganar la apuesta')
