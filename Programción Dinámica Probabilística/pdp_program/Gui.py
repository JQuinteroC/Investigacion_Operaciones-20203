import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class Aplicacion(ttk.Frame):

    def __init__(self):
        ventana = tk.Tk()
        # Configuracion ventana
        super().__init__(ventana)
        ventana.title('Programación dinamica probabilistica')
        
        ventana.configure(width = 610, height = 500)
        self.place(relwidth = 1, relheight = 1)
       # self.root.resizable(width=False, height=False)

        # Declaración de los componentes
        self.iteraciones = ttk.Label(self, text = "N° de iteraciones:", width = 20, font = ("","14"))
        self.iteraciones.place(x = 20, y = 20)

        self.txtIteraciones = ttk.Entry(self, width = 2,font = ("","14"))
        self.txtIteraciones.place(x = 175, y = 20)


        self.anterior = ttk.Label(self, text = f"Restricción:", font = ("", "14"))
        self.anterior.place(x = 225, y = 20)

        self.txtAnterior = ttk.Entry(self, width = 10,font = ("","14"))
        self.txtAnterior.place(x = 470, y = 20)

        self.dec = ttk.Label(self, text=f"1 para maximizar, 2 para minizar:", font=("", "14"))
        self.dec.place(x=20, y=60)

        self.txtDec = ttk.Entry(self, width=2, font=("", "14"))
        self.txtDec.place(x=300, y=60)

        self.respuesta = ScrolledText(self, width = 70, height = 10)
        self.respuesta.place(x = 20, y = 120)
        
        self.btnCalcular = ttk.Button(self, text ='Calcular')
        self.btnCalcular.place(x = 510, y = 80)
        
        
       

