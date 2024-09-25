"""
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
"""

# Solicitar al usuario que ingrese una lista de números separados por comas
numeros = input("Ingresa una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de enteros
lista_numeros = [int(numero) for numero in numeros.split(",")]

# Inicializar contadores para pares e impares
pares = 0
impares = 0

# Recorrer la lista y contar pares e impares
for numero in lista_numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar los resultados
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
