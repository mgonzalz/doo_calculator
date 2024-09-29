from src.calculator import Calculator

def validate_menu(opcion):
    try:
        opcion = int(opcion)
        if opcion < 0 or opcion > 11:
            return False
        return opcion
    except ValueError:
        return False


def main():
    calc = Calculator()
    calc.menu()
    opcion = input("Selecciona una opción: ")
    validar = validate_menu(opcion)
    while validar is False:
        opcion = input("Opción no válida. Debe de ser un opción numérica entre 0 y 11: ")
        validar = validate_menu(opcion)

    opcion = validar
    if opcion == 0:
        print("Salir")
        return
    elif opcion in [1,2,3,4,5]:
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
    else: # [6, 11]
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
        elif opcion == 10:
            print(f"Resultado: {calc.tangente(a)}")
        elif opcion == 11:
            print(f"Resultado: {calc.factorial(a)}")
