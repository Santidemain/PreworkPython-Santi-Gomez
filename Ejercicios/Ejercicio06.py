"""
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)
"""

# Función palíndromo de los apuntes
def es_palindromo(palabra):
  palabra = palabra.lower()
  return palabra == palabra[::-1]

#Pedir al usuario una palabra
palabra = str(input("introduce una palabra:"))

if es_palindromo(palabra):
    print(f"La palabra {palabra} es un palíndromo.")
else:
  print(f"La palabra {palabra} no es un palíndromo.")

