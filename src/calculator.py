import math
class Calculator():
    def __init__(self):
        self.value = 0

    def suma(self, a, b):
        self.value = a + b
        return self.value

    def resta(self, a, b):
        self.value = a - b
        return self.value

    def multiplicacion(self, a, b):
        self.value = a * b
        return self.value

    def division(self, a, b):
        if b == 0:
            return 'Error: Division por cero'
        self.value = a / b
        return self.value

    def potencia(self, a, b):
        self.value = a ** b
        return self.value
    
    def raiz_cuadrada(self, a):
        if a < 0:
            return "Error: Raíz cuadrada de un número negativo"
        self.value = math.sqrt(a)
        return self.value


    def logaritmo(self, a, base=10):
        if a <= 0:
            return "Error: Logaritmo de un número no positivo"
        self.value = math.log(a, base)
        return self.value

    def seno(self, a):
        self.value = math.sin(math.radians(a))
        return self.value

    def coseno(self, a):
        self.value = math.cos(math.radians(a))
        return self.value

    def tangente(self, a):
        self.value = math.tan(math.radians(a))
        return self.value

    def factorial(self, a):
        if a < 0:
            return 'Error: Factorial de numero negativo'
        self.value = 1
        for i in range(1, a + 1):
            self.value *= i
        return self.value
    
    def menu():
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz Cuadrada")
        print("7. Logaritmo")
        print("8. Seno")
        print("9. Coseno")
        print("10. Tangente")
        print("11. Factorial")
        print("0. Salir")

    def __str__(self):
        return str(self.value)
