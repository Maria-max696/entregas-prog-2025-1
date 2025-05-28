#!/usr/bin/env python3

"""
Ejercicio 02: Manipulación básica de fechas con segundos y días.

Este script muestra la fecha actual y permite al usuario añadir
segundos o días a esa fecha.

Autor: Tu Nombre
Correo: tu_correo@ejemplo.com
Fecha: 2025-05-05
"""

from datetime import datetime, timedelta


def manipular_fechas():
    """Menú para manipular fechas añadiendo segundos o días."""
    while True:
        fecha_actual = datetime.now()
        print(f"\n> La fecha actual es: {fecha_actual}")
        print("> Escriba 1 para ingresar segundos, ")
        print(">         2 para ingresar días,")
        print(">         3 para salir.")

        opcion = input("< ")

        if opcion == "1":
            try:
                segundos = int(
                    input("> Escriba la cantidad de segundos\n< ")
                )
                nueva_fecha = fecha_actual + timedelta(seconds=segundos)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print(
                    "> Entrada inválida. Por favor ingrese un número entero."
                )

        elif opcion == "2":
            try:
                dias = int(input("> Escriba la cantidad de días\n< "))
                nueva_fecha = fecha_actual + timedelta(days=dias)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print(
                    "> Entrada inválida. Por favor ingrese un número entero."
                )

        elif opcion == "3":
            print("> Gracias! con python")
            break

        else:
            print("> Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    manipular_fechas()
