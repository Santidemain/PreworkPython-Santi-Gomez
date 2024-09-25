"""
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el usuario.
"""

numeros = input("Ingresa una lista de números separados por comas: ")
lista_numeros = [int(numero) for numero in numeros.split(",")]

suma_total = sum(lista_numeros)
print(f"La suma de los números en la lista es: {suma_total}")

