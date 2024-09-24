"""
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
"""

# Definimos las variables de cada operación
def suma(x,y):
  return (x + y)

def resta(x,y):
  return (x - y)

def multiplicacion(x,y):
  return (x * y)

def division(x,y):
  return (x / y)

def operacion():
  print("Selecciona una opción:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")


while True:
  operacion()    
  eleccion = input("indica el número de la operación o presiona 'e' para salir")
    
  if eleccion == 'e':
    print("gracias por usar la calculadora")
    break
    
  if eleccion in ['1', '2', '3', '4']:
    numero1 = float(input("introduce el primer número: "))
    numero2 = float(input("introduce el segundo número: "))
    
    if eleccion == '1':
        print(f"El resultado es: {suma(numero1,numero2)}")
    elif eleccion == '2':
        print(f"El resultado es: {resta(numero1,numero2)}")
    elif eleccion == '3':
        print(f"El resultado es: {multiplicacion(numero1,numero2)}")
    elif eleccion == '4':
        print(f"El resultado es: {division(numero1,numero2)}")
        
    else:
        print("Opción incorrecta, inténtalo de nuevo")
        
        