# Sistema de Reservas – Fase 4 Programación UNAD

## Descripción del Proyecto

El presente proyecto consiste en el desarrollo de un sistema de reservas implementado en Python, aplicando los principios fundamentales de la Programación Orientada a Objetos (POO).

El sistema permite gestionar diferentes tipos de servicios, tales como:

* Reserva de salas
* Alquiler de equipos
* Asesorías especializadas

Además, el proyecto incorpora manejo de excepciones personalizadas, abstracción, herencia, polimorfismo y registro de errores mediante archivos log.

---

# Objetivos

## Objetivo General

Desarrollar un sistema de reservas utilizando Programación Orientada a Objetos en Python.

## Objetivos Específicos

* Aplicar herencia y polimorfismo en servicios especializados.
* Implementar una clase abstracta para definir comportamientos comunes.
* Gestionar errores mediante excepciones personalizadas.
* Organizar el proyecto utilizando módulos independientes.
* Simular reservas y validaciones dentro del sistema.

---

# Estructura del Proyecto

```bash id="b6k0jk"
fase4-programacion-unad/
│
├── cliente.py
├── servicio.py
├── reserva.py
├── excepciones.py
├── logger.py
├── logs.txt
├── main.py
└── README.md
```

---

# Tecnologías Utilizadas

* Python 3
* Programación Orientada a Objetos
* GitHub
* Logging de Python

---

# Conceptos Aplicados

## Abstracción

Se implementó mediante la clase abstracta `Servicio`.

## Herencia

Las clases `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada` heredan de la clase `Servicio`.

## Polimorfismo

Cada servicio redefine el método `calcular_costo()` según sus características.

## Encapsulamiento

La información y comportamiento de cada entidad se organizó dentro de clases independientes.

## Manejo de Excepciones

Se implementaron excepciones personalizadas para controlar errores del sistema.

---

# Funcionamiento del Sistema

El sistema permite:

1. Registrar clientes.
2. Crear reservas.
3. Calcular costos automáticamente.
4. Confirmar reservas.
5. Cancelar reservas.
6. Detectar errores en operaciones inválidas.
7. Registrar errores en archivos log.

---

# Ejecución del Proyecto

Para ejecutar el sistema:

```bash id="9h9gr9"
python main.py
```

---

# Autor

Proyecto académico desarrollado para Andres Felipe Pirachican Y Isabel Natalia Ariza Bocanegra


