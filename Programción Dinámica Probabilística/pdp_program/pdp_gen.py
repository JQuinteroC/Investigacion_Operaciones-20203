class pdp_gen():

    def __init__(self, probs, costs, sn, xn, type):
        self.probs = probs
        self.costs = costs
        self.sn = sn
        self.xn = xn
        self.type = type  # 1 para max 2 para min
        self.res = ""

    def prob(self, n, xn):
        """
        Retorna la probabilidad

        Args:
            n (int): Número de la etapa
            xn (int): Variable xn

        Returns:
            int: probabilidad de xn para n
        """
        n -= 1

        return self.probs[n][xn]

    def cost(self, n, xn):
        """
        Retorna el costo para xn de n

        Args:
            n (int): Número de la etapa
            xn (int): variable xn

        Returns:
            int: Costo de xn para n
        """
        n -= 1

        return self.costs[n][xn]

    def step_prices(self, n):
        """
        Retorna sn para la etapa n

        Args:
            n (int): Número de la etapa

        Returns:
            int: sn
        """
        n -= 1

        return self.sn[n]

    def step(self, n, last_step, cache):
        """
        Realiza cada una de las operación correspondientes a la iteración dada

        Args:
            n (int): Número de la etapa
            last_step (list[int]): Soluciones optimas para la etapa anterior
            cache (list[list[int]]): Resultados de todos los niveles

        Returns:
            list: Contiene la solución optima
        """
        fn = []
        sn_op, fn_last, xn_op = last_step

        sn = self.step_prices(n)

        for s in sn:  # Calcula los valores de la tabla
            fn_sn = []
            for i in self.xn:
                if s - self.cost(n, i) >= sn_op[0]:  # Si alcanza el dinero para comprar i componentes tipo n
                    j = 0
                    for j, s_last in enumerate(sn_op):  # n -- n + 1
                        if s - self.cost(n, i) == s_last:
                            break
                    fn_sn.append(round(self.prob(n, i) * fn_last[j], 3))
                else:
                    break
            fn.append((s, fn_sn))

        xop_current = []
        values = []

        for (s, fs) in fn:  # Elije los valores optimos para cada valor de s
            x_op = 0
            if self.type == 1:
                value = -10000
                for i, v in zip(self.xn, fs):
                    if v > value:
                        x_op = i
                        value = v
            else:
                value = 10000
                for i, v in zip(self.xn, fs):
                    if v < value:
                        x_op = i
                        value = v
            xop_current.append(x_op)
            values.append(value)

        current_step = (sn, values, xop_current)
        cache.append(current_step)

        if n != 1:
            return self.step(n - 1, current_step, cache)
        else:
            return cache

    def get_sol(self, sol, budget):
        """
        Obtiene la solución más optima y la muestra

        Args:
            sol (list[int]): Cache que contiene las soluciones optimas de cada nivel
            budget (int): máximo disponible
        """
        count = []

        last_step = sol[-1]
        __, prob, __ = last_step

        for j, step in enumerate(reversed(sol)):
            sn, values, xvals = step

            for i in range(len(sn)):
                if sn[i] == budget:
                    count.append(xvals[i])
                    coste = self.cost(j + 1, xvals[i])
                    budget -= coste

        for i in range(len(count)):
            self.res += "x{}: {}. ".format(i + 1, count[i]) + "\n" 

        self.res += "\nLa probabilidad es de: {}%".format(prob[0] * 100)

    def run(self, n, sn_last, v_last, x_last, budget):
        """
        Ejecuta el calculo

        Args:
            n (int): Cantidad de etapas a ejecutar
            sn_last (list[int]): Valores de la etapa de la etapa posterior a la final
            v_last (list[int]): Valores de las vairables de la etapa posterior a la final
            x_last (list[int]): Valores de la variable
            budget (int): Valor máximo permitido
        """
        last_step = (sn_last, v_last, x_last)
        sol = self.step(n, last_step, [])

        self.get_sol(sol, budget)