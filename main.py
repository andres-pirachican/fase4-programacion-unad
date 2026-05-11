from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import DatosInvalidosError, ReservaInvalidaError
from logger import registrar_error

print("Sistema Fase 4 – Programación UNAD")
print("----------------------------------")

# SIMULACIÓN 1: operación válida
try:
    cliente1 = Cliente("Andrés", "123", "andres@correo.com")
    servicio1 = ReservaSala(2, 50000)
    reserva1 = Reserva(cliente1, servicio1)
    print("Reserva 1 confirmada. Costo:", reserva1.confirmar())
except Exception as e:
    registrar_error(str(e))

# SIMULACIÓN 2: operación válida
try:
    servicio2 = AlquilerEquipo(3, 30000)
    reserva2 = Reserva(cliente1, servicio2)
    print("Reserva 2 confirmada. Costo:", reserva2.confirmar())
except Exception as e:
    registrar_error(str(e))

# SIMULACIÓN 3: operación válida
try:
    servicio3 = AsesoriaEspecializada(2, 80000)
    reserva3 = Reserva(cliente1, servicio3)
    print("Reserva 3 confirmada. Costo:", reserva3.confirmar())
except Exception as e:
    registrar_error(str(e))

# SIMULACIÓN 4: error intencional (costo negativo)
try:
    servicio_error = ReservaSala(-1, 50000)
    reserva_error = Reserva(cliente1, servicio_error)
    print("Reserva error confirmada:", reserva_error.confirmar())
except ReservaInvalidaError as e:
    registrar_error(str(e))
    print("Error controlado en reserva")

# SIMULACIÓN 5: cancelación
reserva1.cancelar()
print("Reserva 1 cancelada, estado:", reserva1.estado)

print("Simulación finalizada. El sistema continúa activo.")
