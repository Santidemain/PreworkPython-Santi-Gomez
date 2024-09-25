"""
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
"""

oracion = input("Ingresa una oración: ")
palabras = oracion.split()

numero_de_palabras = len(palabras)

print(f"Número de palabras en la oración: {numero_de_palabras}")

