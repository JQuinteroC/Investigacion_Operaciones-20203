from Gui import Aplicacion
from pdp_gen import pdp_gen


class Controlador():
    def __init__(self, vista):
        self.app = vista
        self.app.btnCalcular['command'] = self.calcular
        self.app.mainloop()

        # Metodo para iniciar el calculo

    def calcular(self):
        n = int(self.app.txtIteraciones.get())
        budget = int(self.app.txtAnterior.get())
        typev = int(self.app.txtDec.get())

        #'''
        #COSECHA
        probs = [[0.5, 0.42, 0.36, 0.25],
                 [0.6, 0.51, 0.41, 0.36],
                 [0.4, 0.35, 0.21, 0.18]]

        costs = [[0, 1, 2, 3],
                 [0, 1, 2, 3],
                 [0, 1, 2, 3]]

        sn = [[4],
              [1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0]]

        xn = [0, 1, 2, 3]

        #typev = 0

        sn_last = [0, 1, 2, 3]
        #budget = 4
        #n = 3
        #'''
        '''
        #CIRCUITO
        probs = [[0, 0.5, 0.6, 0.8],
                 [0, 0.6, 0.7, 0.8],
                 [0, 0.7, 0.8, 0.9],
                 [0, 0.5, 0.7, 0.9]]

        costs = [[0, 100, 200, 300],
                 [0, 200, 400, 500],
                 [0, 100, 300, 400],
                 [0, 200, 300, 400]]

        sn = [[1000],
                       [500, 600, 700, 800, 900],
                       [300, 400, 500, 600, 700],
                       [200, 300, 400, 500, 600],
                       [0]]

        xn = [1, 2, 3]

        #typev = 1 # max

        #budget = 1000

        #n = 4

        sn_last = [0, 100, 200, 300, 400]
        '''

        v_last = []
        x_last = []

        for k in range(n + 1):
            v_last.append(1)
            x_last.append(0)

        prog = pdp_gen(probs, costs, sn, xn, typev)
        prog.run(n, sn_last, v_last, x_last, budget)

    # LLamar a funcion se que calcula y retornar el resultado
    #   solucion = funcion(iteraciones, funcion_inial)
    #   self.app.respuesta.insert("0", solucion)
