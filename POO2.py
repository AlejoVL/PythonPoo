#Herencia
class Vehiculos():
    def __init__(self,_marca,_modelo):
        self.marca = _marca
        self.modelo = _modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def enMarchar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerar: {self.acelera} \nFrenado: {self.frena}")

class Camioneta(Vehiculos):
    def carga(self,_carga):
        self.cargando = _carga
        if self.cargando:
            return "La camioneta está cargada."
        else:
            return "La camioneta aún no está cargada."

class Moto(Vehiculos):
    ruedas = 2
    caballito = ""

    def caballito(self):
        self.caballito = "Voy haciendo piques y no copeo de nada."

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enMarcha} \nAcelerar: {self.acelera} \nFrenado: {self.frena} \nRuedas: {self.ruedas} \n{self.caballito}")

class Vehiculos_electricos(Vehiculos):
    def __init__(self, _marca, _modelo):
        super().__init__(_marca, _modelo)
        self.autonomia = 100

    def carga_energia(self):
        self.cargando = True
        print("Cargando")

    def estado(self):
        super().estado()
        print("Autonomía:",self.autonomia, "Km")

# miMoto = Moto("Yamaha","MT-09")
# miMoto.caballito()
# miMoto.estado()

print("-----------nueva instancia----------")

# miCamioneta = Camioneta("BMW", "X6 M Competition")
# miCamioneta.estado()
# print(miCamioneta.carga(True))

# miCamion = Camioneta("volvo", "233kldfs")
# miCamion.enMarchar()
# miCamion.acelerar()
# miCamion.frenar()
# miCamion.estado()

class Bici_electrica(Vehiculos_electricos, Vehiculos):
    pass

miBici = Bici_electrica("GW", "GW32L")
miBici.estado()
miBici.carga_energia()