"""
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
"""
# Pedir la edad al usuario
edad = int(input("introduce tu edad:"))

if edad >= 18:
  print("Eres mayor de edad")
else:
  print("No puedes pasar")