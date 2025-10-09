def suma(a,b):
    return a+ b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def menu():
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir del programa")

    def menu():
        while True:
            menu()
            try:
                opcion = int(input("Ingrese una opcion: "))
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))

                match opcion:
                    case 1:
                        resultado = suma(num1,num2)
                    case 2:
                        resultado = resta(num1,num2)
                    case 3:
                        resultado = multiplicacion(num1,num2)
                    case 4:
                        resultado = division(num1,num2)
                    case 5:
                        print("Saliendo del programa...")
                        break
                    case _:
                        print("La operacion ingresada no existe.")
            except ValueError:
                print("El valor ingresado no es valido")
            except ZeroDivisionError:
                print("No se puede dividir por 0")
            else:
                print(f"El resultado es: {resultado}")

menu()


