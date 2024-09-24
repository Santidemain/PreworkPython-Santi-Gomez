"""
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
"""

def edad(x,y):
  return(x-y)

añoactual = 2024

añonacimiento = int(input("Introduce tu año de nacimiento: "))
print(f"Tu edad actual es de {edad(añoactual,añonacimiento)} años")
