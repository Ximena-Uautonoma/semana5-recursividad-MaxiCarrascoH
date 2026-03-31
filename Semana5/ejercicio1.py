"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación


    print("-Lista-")
    for i in range(userinput):
        print(1+i)


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    if (n <= 0):
        return n
    else:
        print(n)
        return (contar_recursivo(n-1))


userinput = int(input("Ingrese un numero: "))

contar_ciclo(userinput)

print(contar_recursivo(userinput))