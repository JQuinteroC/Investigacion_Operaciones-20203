from Gui import Aplicacion
from pdp_gen import pdp_gen


class Controlador():
    def __init__(self, vista):
        self.app = vista
        self.app.btnCalcular['command'] = self.calcular
        self.app.btnProba['command'] = self.proba
        self.app.btnCost['command'] = self.cost
        self.app.btnVetp['command'] = self.etapa
        self.app.btnVvar['command'] = self.var
        self.probs = []
        self.costs = []
        self.sn = []
        self.xn = []
        self.app.mainloop()

        # Metodo para iniciar el calculo

    def aceProba(self):
        m = int(self.app.txtProbM.get())
        n = int(self.app.txtProbN.get())
        for i in range(m):
            tem = []
            for j in range(n):
                if j == 0 and i == 0:
                    tem.append(int(self.app.venPro.children['!entry'].get())/100)
                else:
                    tem.append(int(self.app.venPro.children['!entry'+str(j+(i*n)+1)].get())/100)
            self.probs.append(tem)
        self.app.venPro.destroy()
        print(self.probs)
    
    def aceCost(self):
        m = int(self.app.txtCostM.get())
        n = int(self.app.txtCostN.get())
        for i in range(m):
            tem = []
            for j in range(n):
                if j == 0 and i == 0:
                    tem.append(int(self.app.venCosto.children['!entry'].get()))
                else:
                    tem.append(int(self.app.venCosto.children['!entry'+str(j+(i*n)+1)].get()))
            self.costs.append(tem)
        self.app.venCosto.destroy()
        print(self.costs)
    
    def aceEtapa(self):
        m = int(self.app.txtVetpM.get())
        n = int(self.app.txtVetpN.get())
        for i in range(m):
            tem = []
            for j in range(n):
                if j == 0 and i == 0:
                    tem.append(int(self.app.venEtapa.children['!entry'].get()))
                else:
                    tem.append(int(self.app.venEtapa.children['!entry'+str(j+(i*n)+1)].get()))
            for j in range(n-1):
                if tem[j+1] == 0:
                    tem = tem[0:j+1]
                    break
            self.sn.append(tem)
        self.app.venEtapa.destroy()
        print(self.sn)
    
    def aceVar(self):
        m = int(self.app.txtVvarM.get())
        for i in range(1):
            tem = []
            for j in range(m):
                if j == 0 and i == 0:
                    tem.append(int(self.app.venVar.children['!entry'].get()))
                else:
                    tem.append(int(self.app.venVar.children['!entry'+str(j+i+1)].get()))
            for i in range(m):
                self.xn.append(tem[i])
        self.app.venVar.destroy()
        print(self.xn)
    
    def proba(self):
        m = int(self.app.txtProbM.get())
        n = int(self.app.txtProbN.get())
        self.app.Prob(m,n)
        self.app.venPro.children['!button']['command'] = self.aceProba
    
    def cost(self):
        m = int(self.app.txtCostM.get())
        n = int(self.app.txtCostN.get())
        self.app.Costo(m,n)
        self.app.venCosto.children['!button']['command'] = self.aceCost
    
    def etapa(self):
        m = int(self.app.txtVetpM.get())
        n = int(self.app.txtVetpN.get())
        self.app.Etapa(m,n)
        self.app.venEtapa.children['!button']['command'] = self.aceEtapa
    
    def var(self):
        m = int(self.app.txtVvarM.get())
        self.app.Variable(m)
        self.app.venVar.children['!button']['command'] = self.aceVar

    def calcular(self):
        respuesta = ""
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

        #sn_last = [0, 100, 200, 300, 400]
        '''

        v_last = []
        x_last = []

        sn_last = [va - sn[-2][0] for va in sn[-2]]
        while len(sn_last) > n + 1:
            sn_last.pop()
        respuesta += str(sn_last) + "\n"

        for k in range(n + 1):
            v_last.append(1)
            x_last.append(0)

        prog = pdp_gen(self.probs, self.costs, self.sn, self.xn, typev)
        prog.run(n, sn_last, v_last, x_last, budget)
        respuesta += prog.res
        self.app.respuesta.insert("1.0", respuesta)