from src.calculator import Calculator

def menu():
    print('Calculadora')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Potencia')
    print('6. Raíz cuadrada')
    print('7. Logaritmo')
    print('8. Seno')
    print('9. Coseno')
    print('10. Tangente')
    print('11. Factorial')
    print('0. Salir')
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion < 0 or opcion > 11:
                print("Por favor, introduce un número entre 0 y 11.")
                continue
            return opcion
        except ValueError:
            print("Por favor, introduce un número válido.")
def main():
    opcion = menu()
    while opcion != 0:
        calc = Calculator()
        if opcion in [1,2,3,4,5]:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            if opcion == 1:
                print(f"Resultado: {calc.suma(a,b)}")
            elif opcion == 2:
                print(f"Resultado: {calc.resta(a,b)}")
            elif opcion == 3:
                print(f"Resultado: {calc.multiplicacion(a,b)}")
            elif opcion == 4:
                print(f"Resultado: {calc.division(a,b)}")
            elif opcion == 5:
                print(f"Resultado: {calc.potencia(a,b)}")
        elif opcion in [6,7,8,9]:
            a = float(input("Introduce el número: "))
            if opcion == 6:
                print(f"Resultado: {calc.raiz_cuadrada(a)}")
            elif opcion == 7:
                base = float(input("Introduce la base del logaritmo: "))
                print(f"Resultado: {calc.logaritmo(a,base)}")
            elif opcion == 8:
                print(f"Resultado: {calc.seno(a)}")
            elif opcion == 9:
                print(f"Resultado: {calc.coseno(a)}")
        opcion = menu()
