"""
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona. Fórmula: peso (kg) / [estatura (m)]2
"""

def calculo_imc(peso,estatura):
  return(peso / (estatura * estatura))

peso = float(input("Introduce tu peso en Kg: "))
estatura = float(input("Introduce tu estatura en metros:"))

print(f"Tu IMC es de: {calculo_imc(peso,estatura)}")

