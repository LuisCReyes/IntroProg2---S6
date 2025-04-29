# Leer un número ingresado por el usuario
# Mostrar la letra A por cada número del 1 al número
# ingresado por el usuario ejemplo, Número : 3
# a
# aa
# aaa


def mostrarLetras(numero):
    for i in range(1, numero + 1):
        print(f"a" * i)

def main():
    num = int(input("ingrese un numero: "))
    mostrarLetras(num)
    
main()