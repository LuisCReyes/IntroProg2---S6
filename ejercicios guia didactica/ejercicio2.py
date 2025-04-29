"""Contar números pares hasta un límite
Tipo de bucle: mientras
Enunciado: Solicita un número positivo y muestra todos los números pares desde 0 hasta ese
número.
Procedimiento paso a paso:
1. Solicita al usuario un número positivo.
2. Inicializa un contador en 0.
3. Utiliza un bucle mientras que se ejecute mientras el contador sea menor o igual al número
ingresado.
4. En cada iteración, verifica si el contador es par.
5. Si es par, muestra el número.
6. Incrementa el contador en 1.         """

def mostrarPares(numero_positivo):
    for i in range(1, numero_positivo + 1):
        if i % 2 == 0:
            print(i)

def main():
    numero_positivo = int(input("Porfavor ingresá un número positivo: "))
    mostrarPares(numero_positivo)
    
    
main()