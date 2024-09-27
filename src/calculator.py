class Calculator():
    def __init__(self):
        self.value = 0

    def suma(self, a, b):
        self.value = a + b
    
    def resta(self, a, b):
        self.value = a - b

    def multiplicacion(self, a, b):
        self.value = a * b

    def division(self, a, b):
        if b == 0:
            return 'Error: Division por cero'
        self.value = a / b

    def factorial(self, a):
        if a < 0:
            return 'Error: Factorial de numero negativo'
        self.value = 1
        for i in range(1, a + 1):
            self.value *= i

    def __str__(self):
        return str(self.value)
