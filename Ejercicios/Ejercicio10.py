"""
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
"""

diassemana = {1: 'lunes', 2: 'martes', 3: 'miercoles', 4: 'jueves', 5: 'viernes', 6: 'sabado', 7: 'domingo'}

dia = int(input("introduce un número del uno al siete:"))

if 1 <= dia <= 7:
  print(f"El dia indicado es el {diassemana[dia]}")
else:
  print("Has introducido un número incorrecto")
