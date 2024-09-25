"""
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
"""

minutos = int(input("Introduce el número de minutos: "))
horas = minutos // 60
minutos_resto = minutos % 60

print(f"{minutos} minutos equivalen a {horas} horas y {minutos_resto} minutos")




