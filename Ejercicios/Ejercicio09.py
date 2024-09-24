"""
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
"""

euro = 0.85

def dolar_euro(x, y):
  return(x / y)

dolares = float(input("Introduce la cantidad de dólares a convertir:"))
print(f"Tus dólares equivalen a {dolar_euro(dolares,euro)} euros")

