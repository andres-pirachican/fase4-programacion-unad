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
# Servicios especializados

class ReservaSala(Servicio):
    def __init__(self, horas, costo_hora):
        self.horas = horas
        self.costo_hora = costo_hora

    def calcular_costo(self):
        return self.horas * self.costo_hora

    def describir_servicio(self):
        return "Reserva de sala"


class AlquilerEquipo(Servicio):
    def __init__(self, dias, costo_dia):
        self.dias = dias
        self.costo_dia = costo_dia

    def calcular_costo(self):
        return self.dias * self.costo_dia

    def describir_servicio(self):
        return "Alquiler de equipo"


class AsesoriaEspecializada(Servicio):
    def __init__(self, sesiones, costo_sesion):
        self.sesiones = sesiones
        self.costo_sesion = costo_sesion

    def calcular_costo(self):
        return self.sesiones * self.costo_sesion

    def describir_servicio(self):
        return "Asesoría especializada"
