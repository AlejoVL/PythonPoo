class Persona():
    def __init__(self,_nombre,_edad,_residencia):
        self.nombre = _nombre
        self.edad = _edad
        self.residencia = _residencia

    def descripcion(self):
        print("Nombre:",self.nombre, "\nEdad:",self.edad, "\nResidencia:",self.residencia)

class Empleado(Persona):
    def __init__(self,_nombre,_edad,_residencia, _salario, _antiguedad):
        #Se llama el metodo padre constructor
        super().__init__(_nombre, _edad, _residencia)
        self.salario = _salario
        self.antiguedad = _antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:",self.salario, "\nAntiguedad:",self.antiguedad)
        
empleado1 = Empleado("Alejandro", 21, "Medellin", 1000000, 4)
empleado1.descripcion()