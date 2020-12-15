from Gui import Aplicacion

class Controlador():
    def __init__(self, vista):
        self.app = vista
        self.app.btnCalcular['command'] = self.calcular
        self.app.mainloop()        

    # Metodo para iniciar el calculo     
    def calcular(self):
        iteraciones = self.app.txtIteraciones.getInt()
        funcion_inicial = self.app.txtAnterior.getInt()

        # LLamar a funcion se que calcula y retornar el resultado
    #   solucion = funcion(iteraciones, funcion_inial)
    #   self.app.respuesta.insert("0", solucion)