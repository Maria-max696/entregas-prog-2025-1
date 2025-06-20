#!/usr/bin/env python3

"""
Ejercicio 02: Menú de manipulación de texto

Este script permite al usuario manipular una cadena de texto
de diferentes formas:
- Convertir a minúsculas
- Convertir a mayúsculas
- Invertir mayúsculas y minúsculas
- Capitalizar (primera letra en mayúscula)
- Titular (cada palabra inicia con mayúscula)
- Reemplazar espacios por guiones bajos

Autor: Maria Paula Galvis Orjuela <mariapaulagalvisorjuela701@gmail.com>
Fecha: 2025-05-24
"""


def run():
    """Punto de entrada del script"""
    # Solicitar al usuario una cadena de texto
    texto = input("< Ingrese una cadena de texto: ")

    while True:
        # Mostrar el menú de opciones
        print("\n> Escriba 1 para pasar a minúsculas,")
        print("> 2 para pasar a mayúsculas,")
        print("> 3 para invertir mayúsculas y minúsculas")
        print("> 4 para pasar a capitalización.")
        print("> 5 para pasar a titulación.")
        print("> 6 para reemplazar espacios por guiones bajos.")
        print("> 7 para salir.")

        opcion = input("> < ")

        # Ejecutar la opción seleccionada
        if opcion == "1":
            print(f"> Resultado: {texto.lower()}")
        elif opcion == "2":
            print(f"> Resultado: {texto.upper()}")
        elif opcion == "3":
            print(f"> Resultado: {texto.swapcase()}")
        elif opcion == "4":
            print(f"> Resultado: {texto.capitalize()}")
        elif opcion == "5":
            print(f"> Resultado: {texto.title()}")
        elif opcion == "6":
            print(f"> Resultado: {texto.replace(' ', '_')}")
        elif opcion == "7":
            print("> ¡Gracias por usar el programa!")
            break
        else:
            print("> Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    run()
