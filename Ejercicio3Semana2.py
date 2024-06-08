from abc import *

class Empleado(ABC):
    def __init__(self, id_trabajador, salario):
        self.id_trabajador = id_trabajador
        self.salario = salario

    @abstractmethod
    def calcularSalario(self):
        pass
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, id_trabajador, salario, estimulo):
        super().__init__(id_trabajador, salario)
        self.estimulo = estimulo

    def calcularSalario(self):
        return self.salario + self.salario * self.estimulo
        
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, id_trabajador, salario, horas_extra):
        super().__init__(id_trabajador, salario)
        self.horas_extra = horas_extra

    def calcularSalario(self):
        return self.salario + (self.salario * 0.25) * self.horas_extra
    
class Contratista(Empleado):
    def __init__(self, id_trabajador, salario, utilidades):
        super().__init__(id_trabajador, salario)
        self.utilidades = utilidades

    def calcularSalario(self):
        return self.salario + self.salario * self.utilidades


empleados = {
    EmpleadoMedioTiempo("Soy empleado a medio tiempo", 1500, 2), 
    EmpleadoTiempoCompleto("Soy empleado a tiempo completo", 3000, 0.25),
    Contratista("Soy un contratista", 4000, 1.75)
}

for empleado in empleados:
   print(empleado.calcularSalario())


