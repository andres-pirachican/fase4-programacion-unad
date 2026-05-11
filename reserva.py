from excepciones import ReservaInvalidaError

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "PENDIENTE"

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo()
            if costo <= 0:
                raise ReservaInvalidaError("El costo no puede ser negativo")
            self.estado = "CONFIRMADA"
            return costo
        except ReservaInvalidaError as e:
            self.estado = "ERROR"
            raise e
        finally:
            pass

    def cancelar(self):
        self.estado = "CANCELADA"
