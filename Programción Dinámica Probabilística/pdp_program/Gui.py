import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class Aplicacion(ttk.Frame):

    def __init__(self):
        ventana = tk.Tk()
        # Configuracion ventana
        super().__init__(ventana)
        ventana.title('Programación dinamica probabilistica')
        
        ventana.configure(width = 610, height = 440)
        self.place(relwidth = 1, relheight = 1)
       # self.root.resizable(width=False, height=False)

        # Declaración de los componentes
        ## Iteraciones
        self.iteraciones = ttk.Label(self, text = "N° de iteraciones:", width = 20, font = ("","14"))
        self.iteraciones.place(x = 20, y = 20)
        self.txtIteraciones = ttk.Entry(self, width = 2,font = ("","14"))
        self.txtIteraciones.place(x = 175, y = 20)

        ## Maximizar o minimizar
        self.dec = ttk.Label(self, text="1 para maximizar, 2 para minimizar:", font=("", "14"))
        self.dec.place(x=260, y=20)
        self.txtDec = ttk.Entry(self, width=2, font=("", "14"))
        self.txtDec.place(x=560, y=20)

        ## Restricción
        self.anterior = ttk.Label(self, text = f"Restricción:", font = ("", "14"))
        self.anterior.place(x = 20, y = 60)
        self.txtAnterior = ttk.Entry(self, width = 10,font = ("","14"))
        self.txtAnterior.place(x = 130, y = 60)

        ## Matriz probabilidades
        self.prob = ttk.Label(self, text="Probabilidades MxN:", font=("", "14"))
        self.prob.place(x=20, y=100)
        self.txtProbM = ttk.Entry(self, width=2,font=("", "14"))
        self.txtProbM.place(x=200, y=100)
        self.txtProbN = ttk.Entry(self, width=2,font=("", "14"))
        self.txtProbN.place(x=230, y=100)
        self.btnProba = ttk.Button(self, text = "Probabilidades")
        self.btnProba.place(x=270, y=100)

        ## Matriz costos
        self.cost = ttk.Label(self, text="Costos MxN:", font=("", "14"))
        self.cost.place(x=20, y=140)
        self.txtCostM = ttk.Entry(self, width=2,font=("", "14"))
        self.txtCostM.place(x=135, y=140)
        self.txtCostN = ttk.Entry(self, width=2,font=("", "14"))
        self.txtCostN.place(x=165, y=140)
        self.btnCost = ttk.Button(self, text = "Costos")
        self.btnCost.place(x=205, y=140)

        ## Matriz valores por etapa
        self.vetp = ttk.Label(self, text="Valores etapa MxN:", font=("", "14"))
        self.vetp.place(x=20, y=180)
        self.txtVetpM = ttk.Entry(self, width=2,font=("", "14"))
        self.txtVetpM.place(x=190, y=180)
        self.txtVetpN = ttk.Entry(self, width=2,font=("", "14"))
        self.txtVetpN.place(x=220, y=180)
        self.btnVetp = ttk.Button(self, text = "Etapas")
        self.btnVetp.place(x=260, y=180)

        ## Matriz valores por variable
        self.vvar = ttk.Label(self, text="Valores variable 1xM:", font=("", "14"))
        self.vvar.place(x=20, y=220)
        self.txtVvarM = ttk.Entry(self, width=2,font=("", "14"))
        self.txtVvarM.place(x=210, y=220)
        self.btnVvar = ttk.Button(self, text = "Variables")
        self.btnVvar.place(x=250, y=220)

        # Componente de respuesta
        self.respuesta = ScrolledText(self, width = 70, height = 8)
        self.respuesta.place(x = 20, y = 260)
        
        # Boton de calcular
        self.btnCalcular = ttk.Button(self, text ='Calcular')
        self.btnCalcular.place(x = 510, y = 400)
    
    def Prob(self, m, n):
        """
        Crea la ventana con MxN entradas para la creación de la matriz de probabilidades

        Args:
            m (int): valor M de la matriz
            n (int): valor N de la matriz
        """
        self.venPro = tk.Tk()
        for r in range(0, m):
            for c in range(0, n):
                cell = ttk.Entry(self.venPro, width=8)
                cell.grid(padx=m, pady=n, row=r, column=c)
        self.venPro.title("Probabilidades")
        btnAceptarPro = ttk.Button(self.venPro, text ='Aceptar')
        btnAceptarPro.grid(padx=m+1, pady=1, row=m, column=0)
    
    def Costo(self, m, n):
        """
        Crea la ventana con MxN entradas para la creación de la matriz de costos

        Args:
            m (int): valor M de la matriz
            n (int): valor N de la matriz
        """
        self.venCosto = tk.Tk()
        for r in range(0, m):
            for c in range(0, n):
                cell = ttk.Entry(self.venCosto, width=8)
                cell.grid(padx=m, pady=n, row=r, column=c)
        self.venCosto.title("Costos")
        btnAceptarCost = ttk.Button(self.venCosto, text ='Aceptar')
        btnAceptarCost.grid(padx=m+1, pady=1, row=m, column=0)
    
    def Etapa(self, m, n):
        """
        Crea la ventana con MxN entradas para la creación de la matriz de valores por etapa

        Args:
            m (int): valor M de la matriz
            n (int): valor N de la matriz
        """
        self.venEtapa = tk.Tk()
        for r in range(0, m):
            for c in range(0, n):
                cell = ttk.Entry(self.venEtapa, width=8)
                cell.grid(padx=m, pady=n, row=r, column=c)
        self.venEtapa.title("Etapa")
        btnAceptarEtp = ttk.Button(self.venEtapa, text ='Aceptar')
        btnAceptarEtp.grid(padx=m+1, pady=1, row=m, column=0)
    
    def Variable(self, m):
        """
        Crea la ventana con 1xM entradas para la creación de la valores por variable

        Args:
            m (int): valor M de la matriz
        """
        self.venVar = tk.Tk()
        for r in range(0, 1):
            for c in range(0, m):
                cell = ttk.Entry(self.venVar, width=8)
                cell.grid(padx=1, pady=m, row=r, column=c)
        self.venVar.title("Variable")
        btnAceptarCost = ttk.Button(self.venVar, text ='Aceptar')
        btnAceptarCost.grid(padx=2, pady=1, row=1, column=0)