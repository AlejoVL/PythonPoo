class Padre():
    def __init__(self, _labios, _cabello):
        self.labios = _labios
        self.cabello = _cabello

class Hijo(Padre):
    def __init__(self, _labios, _cabello, _cara):
        super().__init__(_labios, _cabello)
        self.cara = _cara

Alejo = Hijo("Gruesos", "Ondulado", "Razgos irlandeces")
print("Sus labios son: {} \nSus cejas son: {} \nSu cara es de: {}".format(Alejo.labios, Alejo.cabello, Alejo.cara))
print("Salio lindo como el papá.")