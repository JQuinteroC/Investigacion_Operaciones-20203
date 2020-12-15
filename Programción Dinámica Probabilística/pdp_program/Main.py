from Controller import Controlador
from Gui import Aplicacion

class programaPDP():
    def __init__(self):
        v = Aplicacion()
        c = Controlador(v)

def main():
    programaPDP()
    return 0

if __name__ == '__main__':
    main()