#!/usr/bin/env python
def ejecutar():
    """Punto de entrada del script"""
    calculadora()
"""
Calculadora 1: prototipo básico

Este es un ejemplo de demostración del uso de la plantilla 
en programación.

Autor: Maria Paula Galvis Orjuela <mariapaulagalvisorjuela701@gmail.com>
Fecha: 2025-03-27
"""

def formatear_resultado(resultado):
    """Devuelve el resultado como entero si no tiene decimales, de lo contrario, como flotante."""
    return int(resultado) if resultado.is_integer() else resultado

def calculadora():
    """Ejecuta la calculadora interactiva"""
    
    print("Escoge una operación: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    seleccion = input("Bienvenida, selecciona tu operación entre 1/2/3/4: ")
    
    valor_a = float(input("Escribe un número: "))
    valor_b = float(input("Escribe otro número: "))

    if seleccion == '1':
        resultado = valor_a + valor_b
        print(f"La suma de {valor_a} y {valor_b} es {formatear_resultado(resultado)}")

    elif seleccion == '2':
        resultado = valor_a - valor_b
        print(f"La resta de {valor_a} y {valor_b} es {formatear_resultado(resultado)}")

    elif seleccion == '3':
        resultado = valor_a * valor_b
        print(f"La multiplicación de {valor_a} y {valor_b} es {formatear_resultado(resultado)}")

    elif seleccion == '4':
        if valor_b != 0:
            resultado = valor_a / valor_b
            print(f"La división de {valor_a} entre {valor_b} es {formatear_resultado(resultado)}")
        else:
            print("Error: No se puede dividir por cero.")

    else:
        print("Error: Selecciona una opción válida (1/2/3/4).")
if __name__ == "__main__":
    ejecutar()

