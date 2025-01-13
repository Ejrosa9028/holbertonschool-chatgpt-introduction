#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementamos n para evitar un bucle infinito
    return result

# Verificamos que el argumento haya sido pasado
if len(sys.argv) > 1:
    f = factorial(int(sys.argv[1]))  # Convertimos el argumento a entero
    print(f)
else:
    print("Por favor, ingresa un número como argumento.")
