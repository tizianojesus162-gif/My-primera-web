from abc import ABC, abstractmethod


# Clase abstracta
class Trabajador(ABC):

    def __init__(self, nombre, salario_base):
        self._nombre = nombre
        self._salario_base = salario_base

    # Getter para acceder al nombre
    @property
    def nombre(self):
        return self._nombre

    # Método abstracto
    @abstractmethod
    def calcular_salario_neto(self):
        pass


# Clase Desarrollador
class Desarrollador(Trabajador):

    def __init__(self, nombre, salario_base, proyectos_terminados):
        super().__init__(nombre, salario_base)
        self.proyectos_terminados = proyectos_terminados

    def calcular_salario_neto(self):
        return self._salario_base + (15000 * self.proyectos_terminados)


# Clase Gerente
class Gerente(Trabajador):

    def __init__(self, nombre, salario_base, bono_fijo):
        super().__init__(nombre, salario_base)
        self.bono_fijo = bono_fijo

    def calcular_salario_neto(self):
        return self._salario_base + self.bono_fijo


# Crear un desarrollador
desarrollador = Desarrollador(
    "Juan",
    500000,
    3
)


# Crear un gerente
gerente = Gerente(
    "Carlos",
    800000,
    100000
)


# Mostrar resultados
print("Empleado:", desarrollador.nombre)
print("Salario neto:", desarrollador.calcular_salario_neto())

print()

print("Empleado:", gerente.nombre)
print("Salario neto:", gerente.calcular_salario_neto())