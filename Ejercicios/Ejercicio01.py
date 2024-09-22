"""
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
"""

# Convertir de Celsius a Farenheit
def celsius_farenheit(celsius):
  return (celsius*1.8) + 32

# Pedir la temperatura en grados celsius
celsius = float(input("introduce la temperatura en grados celsius:"))

Farenheit = celsius_farenheit(celsius)

print(f"{celsius} grados Celsius son {Farenheit} grados Farenheit")