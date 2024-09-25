"""
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
"""

def precio_final(x, y):
  return(x * y)
descuento = 0.8

Precio = float(input ("introduce el precio del artículo: "))

print(f"El precio final con el descuento  es de {precio_final(Precio, descuento)} euros")