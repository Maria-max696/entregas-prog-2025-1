#!/usr/bin/env python3

"""
Calculadora 2: prototipo básico

Este es un ejemplo de demostración del uso de la plantilla
en programación.

Autor: Maria Paula Galvis Orjuela <mariapaulagalvisorjuela701@gmail.com>
Fecha: 2025-04-03
"""


def formatear_resultado(resultado):
    """Devuelve el resultado como entero si no tiene decimales,
    de lo contrario, como flotante.
    """
    return int(resultado) if resultado.is_integer() else resultado


def solicitar_numero(mensaje):
    """Solicita un número al usuario sin validación."""
    entrada = input(mensaje).strip()
    if entrada == "":
        return None
    return float(entrada)


def calculadora():
    """Ejecuta la calculadora interactiva con repetición"""

    while True:
        print(
            "\nEscriba 1 para suma, \n"
            "        2 para resta, \n"
            "        3 para multiplicación \n"
            "        4 para división.\n"
            "        5 para potenciación.\n"
            "        6 para división entera.\n"
            "        7 para módulo.\n"
            "        8 para salir."
        )

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "8":
            print("Gracias!")
            break

        if opcion not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Opción inválida.")
            continue

        operando_a = solicitar_numero(
            "Ingrese el operando A (vacío para cancelar): "
        )
        if operando_a is None:
            print("Operación cancelada")
            continue

        operando_b = solicitar_numero(
            "Ingrese el operando B (vacío para cancelar): "
        )
        if operando_b is None:
            print("Operación cancelada")
            continue

        if opcion == "1":
            resultado = operando_a + operando_b
            print(
                f"El resultado de la suma es: "
                f"{formatear_resultado(resultado)}"
            )
        elif opcion == "2":
            resultado = operando_a - operando_b
            print(
                f"El resultado de la resta es: "
                f"{formatear_resultado(resultado)}"
            )
        elif opcion == "3":
            resultado = operando_a * operando_b
            print(
                f"El resultado de la multiplicación es: "
                f"{formatear_resultado(resultado)}"
            )
        elif opcion == "4":
            if operando_b != 0:
                resultado = operando_a / operando_b
                print(
                    f"El resultado de la división es: "
                    f"{formatear_resultado(resultado)}"
                )
            else:
                print("Error: No se puede dividir por cero.")
        elif opcion == "5":
            resultado = operando_a ** operando_b
            print(
                f"El resultado de la potenciación es: "
                f"{formatear_resultado(resultado)}"
            )
        elif opcion == "6":
            if operando_b != 0:
                resultado = operando_a // operando_b
                print(
                    f"El resultado de la división entera es: "
                    f"{formatear_resultado(resultado)}"
                )
            else:
                print("Error: No se puede dividir por cero.")
        elif opcion == "7":
            if operando_b != 0:
                resultado = operando_a % operando_b
                print(
                    f"El resultado del módulo es: "
                    f"{formatear_resultado(resultado)}"
                )
            else:
                print(
                    "Error: No se puede calcular el módulo con "
                    "divisor cero."
                )


def ejecutar():
    """Punto de entrada del script"""
    calculadora()


if __name__ == "__main__":
    ejecutar()
