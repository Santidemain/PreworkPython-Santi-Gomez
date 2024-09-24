"""
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
"""

def area_rectangulo(x,y):
  return(x * y)

longitud = int(input("Introduce la longitud del rectángulo: "))
Anchura = int(input("Introduce la anchura del rectángulo: "))

print(f"El área del rectángulo es de {area_rectangulo(longitud,Anchura)} unidades")