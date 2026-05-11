#Clase abstracta Servicio
#Fase 4 - Programación UNAD

from abc import ABC, abstractmethod

class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass
