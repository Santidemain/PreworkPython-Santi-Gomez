"""
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
"""

#Pongo un contador en marcha
suma = 0

# Un bucle para no definir todos los números a mano
for numero in range(1, 101):
  if numero % 2 == 0:
    suma += numero
    
print("La suma de los números pares del 1 al 100 es:", suma)
