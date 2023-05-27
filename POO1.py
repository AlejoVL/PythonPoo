class Coche():
    #propiedades,estados,comportamientos
    #constructor
    def __init__(self):
        self.__largoChasis = 3.5
        self.__anchoChasis = 2
        self.__ruedas = 4
        self.__enMarcha = False

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "ok"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "ok":
            return True
        else:
            return False

    def arrancar(self,_arrancamos):
        self.__enMarcha = _arrancamos        
        if(self.__enMarcha):
            chequeo = self.chequeo_interno()

        if self.__enMarcha and chequeo:
            return "El coche está en marcha"
        
        elif self.__enMarcha and chequeo == False:
            return "Error! algo salió mal con el chequeo, por lo tanto no se puede arrancar."
        
        else:
            return "El coche está parado"

    def estado(self):
        print("El largo del coche es:",self.__largoChasis, "\nEl ancho del coche es:",self.__anchoChasis, "\nLa cantidad de ruedas es:",self.__ruedas)
        
#instacia de la clase
# miCoche1 = Coche()
# print("El largo del coche es:",miCoche1.largoChasis)
# print("El ancho del coche es:",miCoche1.anchoChasis)
# print("La cantidad de ruedas es:",miCoche1.ruedas)
#print(miCoche1.estado())

print("---------------------Nueva---------------------")

# miCoche1 = Coche()
# miCoche1.ruedas = 3
# miCoche1.estado()

# print(miCoche1.arrancar(False))

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()
print(miCoche.__chequeo_interno())