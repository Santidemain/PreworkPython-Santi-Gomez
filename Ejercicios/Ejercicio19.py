"""
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
"""

# Solicitar al usuario que ingrese un año
año = int(input("Ingresa un año: "))

# Verificar si el año es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")
