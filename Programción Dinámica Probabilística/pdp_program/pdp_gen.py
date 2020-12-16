class pdp_gen():

    def __init__(self, probs, costs, sn, xn, type):
        self.probs = probs
        self.costs = costs
        self.sn = sn
        self.xn = xn
        self.type = type  # 1 para max 2 para min

    def prob(self, n, xn):
        '''

        Retorna la probabilidad
        Args:
            n: número de la etapa
            xn: variable xn

        Returns: probabilidad de xn para n

        '''

        n -= 1
        #xn -= 1

        return self.probs[n][xn]

    def cost(self, n, xn):
        '''

        Retorna el costo para xn de n
        Args:
            n: número de la etapa
            xn: variable xn

        Returns: costo de xn para n

        '''

        n -= 1
        #xn -= 1

        return self.costs[n][xn]

    def step_prices(self, n):
        '''

        Retorna sn para la etapa n
        Args:
            n: número de la etapa

        Returns: sn

        '''

        n -= 1

        return self.sn[n]

    def step(self, n, last_step, cache):
        '''

        Args:
            n: número de la etapa
            last_step: soluciones optimas para la etapa anterior
            cache: resultados de todos los niveles

        Returns: tupla que contiene la solución optima

        '''

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
                #print('entra a max')
                value = -10000
                for i, v in zip(self.xn, fs):
                    if v > value:
                        x_op = i
                        value = v
                        #print(x_op, value)
            else:
                #print('entra a min')
                value = 10000
                for i, v in zip(self.xn, fs):
                    if v < value:
                        x_op = i
                        value = v
                        #print(x_op, value)
            xop_current.append(x_op)
            values.append(value)

        current_step = (sn, values, xop_current)
        cache.append(current_step)

        if n != 1:
            return self.step(n - 1, current_step, cache)
        else:
            return cache

    def get_sol(self, sol, budget):
        '''
        Obtiene la solución más optima y la muestra
        Args:
            sol: cache que contiene las soluciones optimas de cada nivel
            budget: máximo disponible
        Returns: None
        '''

        count = []

        last_step = sol[-1]
        __, prob, __ = last_step

        for j, step in enumerate(reversed(sol)):
            sn, values, xvals = step

            for i in range(len(sn)):
                if sn[i] == budget:
                    count.append(xvals[i])
                    #print(j + 1, xvals[i])
                    coste = self.cost(j + 1, xvals[i])
                    budget -= coste

        for i in range(len(count)):
            print("x{}: {}. ".format(i + 1, count[i]))

        print("\nLa probabilidad es de: {}%".format(prob[0] * 100))

    def run(self, n, sn_last, v_last, x_last, budget):
        '''
        Ejecuta el calculo
        Args:
            n: cantidad de etapas a ejecutar
            sn_last: Sn de la etapa posterior a la final
            v_last: Valores de la etapa posterior a la final

        Returns: None
        '''
        last_step = (sn_last, v_last, x_last)
        sol = self.step(n, last_step, [])

        self.get_sol(sol, budget)