# Sistema de Reservas – Fase 4 Programación UNAD

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema de reservas implementado en Python, aplicando los conceptos fundamentales de Programación Orientada a Objetos (POO).

El sistema permite gestionar reservas de diferentes tipos de servicios, incluyendo:

* Reserva de salas
* Alquiler de equipos
* Asesorías especializadas

Además, el proyecto implementa manejo de excepciones personalizadas, abstracción, herencia, polimorfismo y modularización del código.

---

## Objetivos del Proyecto

* Aplicar los conceptos de Programación Orientada a Objetos.
* Implementar herencia y polimorfismo mediante servicios especializados.
* Utilizar clases abstractas y excepciones personalizadas.
* Simular el funcionamiento de un sistema de reservas.
* Organizar el código en módulos reutilizables.

---

## Estructura del Proyecto

```bash
fase4-programacion-unad/
│
├── cliente.py
├── servicio.py
├── reserva.py
├── excepciones.py
├── logger.py
├── main.py
└── README.md
```

---

## Tecnologías Utilizadas

* Python 3
* Programación Orientada a Objetos
* Manejo de excepciones
* GitHub

---

## Conceptos Aplicados

### Abstracción

Se implementó mediante la clase abstracta `Servicio`.

### Herencia

Las clases `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada` heredan de `Servicio`.

### Polimorfismo

Cada servicio redefine el método `calcular_costo()` según sus necesidades.

### Encapsulamiento

Los atributos y métodos se organizan dentro de clases para proteger la lógica del sistema.

### Manejo de Excepciones

Se utilizan excepciones personalizadas para controlar errores durante las reservas.

---

## Ejecución del Proyecto

Para ejecutar el sistema:

```bash
python main.py
```

---

## Autor

Proyecto académico desarrollado por Andres Felipe Pirachican y Isabel Natalia Ariza Bocanegra

