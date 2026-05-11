#Excepciones personalizadas del sistema
#Fase 4 - Programación UNAD

class DatosInvalidosError(Exception):
    """Se genera cuando los datos ingresados no son válidos."""
    pass


class ServicioNoDisponibleError(Exception):
    """Se genera cuando el servicio solicitado no está disponible."""
    pass


class ReservaInvalidaError(Exception):
    """Se genera cuando ocurre un error en el proceso de reserva."""
    pass
