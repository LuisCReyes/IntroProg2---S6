# Tabla de multiplicar según el número ingresado


def tablaMultiplicar(numero):
    print(f"Tabla de multiplicar del número {numero}")
    for i in range(1, 12):
        num2 = numero * i
        print(numero, "*", i, "=", num2)
        
def main():
    numero = int(input("Ingrese un número: "))
    tablaMultiplicar(numero)
    
    
main()