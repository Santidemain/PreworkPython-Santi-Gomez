"""
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
"""
# Definimos la palabra, vocales y un contador
palabra = str(input("introduce una palabra:"))
vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in palabra:
  if letra in vocales:
    contador_vocales +=1

print(f"El número de vocales en tu palabSra es: {contador_vocales}")



