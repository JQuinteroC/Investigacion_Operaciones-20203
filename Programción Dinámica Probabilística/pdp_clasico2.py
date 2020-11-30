def prob(n, xn):
    '''
    Retorna la probabilidad del componente dado
    Args:
        n: número de la etapa
        xn: cantidad de unidades paralelas
    Returns: probabilidad de que el componente n funcione con x unidades paralelas
    '''

    n -= 1

    probs = [[0.5, 0.42, 0.36, 0.25],
             [0.6, 0.51, 0.41, 0.36],
             [0.4, 0.35, 0.21, 0.18]]

    return probs[n][xn]


def cost(n, xn):
    '''
    Retorna el precio asociado a instalar xn unidades del componente n
    Args:
        n: número de la etapa
        xn: cantidad de unidades paralelas
    Returns: precio de instalar xn unidades del componente n
    '''

    n -= 1

    price = [[0, 1, 2, 3],
             [0, 1, 2, 3],
             [0, 1, 2, 3]]

    return price[n][xn]


def step_prices(n):
    '''
    Retorna el dinero disponible asociado a cada etapa
    Args:
        n: número de la etapa
    Returns: cantidades de dinero disponible para la etapa n
    '''

    n -= 1

    step_prices = [[4],
                   [1, 2, 3, 4],
                   [0, 1, 2, 3, 4],
                   [0]]

    return step_prices[n]

def step(n, last_step, cache):
    '''
    Args:
        n: número de la etapa
        last_step: soluciones optimas para la etapa anterior
        cache: resultados de todos los niveles
    Returns: tupla que contiene la solución optima
    '''

    fn = []
    sn_op, fn_last, xn_op = last_step

    sn = step_prices(n)

    for s in sn: # Calcula los valores de la tabla
        fn_sn = []
        for i in range(0, 4):
            if s - cost(n, i) >= sn_op[0]: # Si alcanzan los dias
                j = 0
                for j, s_last in enumerate(sn_op):  # n -- n + 1
                    if s - cost(n, i) == s_last:
                        break
                fn_sn.append(round(prob(n, i) * fn_last[j], 3))
            else:
                break
        #print(fn_sn)
        fn.append((s, fn_sn))

    xop_current = []
    values = []

    for (s, fs) in fn: #Elije los valores optimos para cada valor de s
        x_op = 0
        value = 10000
        for i, v in enumerate(fs):
            if v < value:
                x_op = i
                value = v
        xop_current.append(x_op)
        values.append(value)

    current_step = (sn, values, xop_current)
    cache.append(current_step)

    if n != 1:
        return step(n - 1, current_step, cache)

    else:
        return cache

def get_sol(sol):
    '''
    Obtiene la solución más optima y la muestra
    Args:
        sol: cache que contiene las soluciones optimas de cada nivel
    Returns: None
    '''

    budget = 4
    count = []

    last_step = sol[-1]
    __, prob, __ = last_step

    for j, step in enumerate(reversed(sol)):
        sn, values, xvals = step

        for i in range(len(sn)):
            if sn[i] == budget:
                count.append(xvals[i])
                coste = cost(j + 1, xvals[i])
                budget -= coste

    nombres = ["Poda", "Raleo", "Cosecha"]

    print("La asignación optima de dias es:")
    for i in range(len(count)):
        print(f"Dedicar {count[i]} dia(s) a la {nombres[i]}")

    print("\n")

    for i in range(len(count)):
        print("x{}: {}. ".format(i + 1, count[i]))

    print("\nLa probabilidad de ser despedido es de: {}%".format(prob[0] * 100))


def main():
    n = 3

    sn_3 = [0, 1, 2, 3]
    v_3 = [1, 1, 1, 1]
    x_3 = [0, 0, 0, 0]
    step_3 = (sn_3, v_3, x_3)

    sol = step(n, step_3, [])

    get_sol(sol)

if __name__ == "__main__":
    main()
