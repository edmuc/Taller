#PAGINA 3
# 1
def cuadrado_positivo():
    n = 0
    while n >= 0:
        n = int(input("Ingrese un número: "))
        if n >= 0:
            print("El cuadrado es:", n * n)
        else:
            print("Número negativo, fin del programa.")

cuadrado_positivo()

# 2
def xy():
    n = int(input("Ingrese un número entero positivo: "))
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end=" ")
xy()

# 3
def poblacion():
    A = 25_000_000
    B = 18_900_000
    año = 2022
    while B <= A:
        A = A + (A * 2 / 100)
        B = B + (B * 3 / 100)
        año = año + 1
    print("El país B superará al país A en el año", año)
poblacion()

#PAGINA 4

def epsilon_maquina():
    epsilon = 1.0
    while 1.0 + epsilon != 1.0:
        epsilon = epsilon / 2.0
    epsilon = epsilon * 2.0
    print("El épsilon de la máquina es:", epsilon)
epsilon_maquina()

#PAGINA 5

#Ejercicio 1

for i in range(1, 101):
    print(i, "cuadrado =", i * i)


#Ejercicio 2

# Impares del 1 al 999
print("Números impares del 1 al 999:")
for i in range(1, 1000):
    if i % 2 != 0:
        print(i)

# Pares del 2 al 1000
print("\nNúmeros pares del 2 al 1000:")
for i in range(2, 1001):
    if i % 2 == 0:
        print(i)


#Ejercicio 3
#Imprimir los numeros pares en forma descendente hasta 2 que son menores o iguales a un n ́umero natural n ≥ 2 dado.

Numero=int(input("Ingrese un numero:"))
for i in range(Numero,1,-1):
    if i%2==0:
        print(i)


#Ejercicio 4
#Imprimir los numeros de 1 hasta un numero natural n dado, cada uno con su respectivo factorial.

n = int(input("Ingrese un número natural: "))

for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial = factorial * j
    print(i, "factorial =", factorial)

#Ejercicio 5
#Calcular el valor de 2 elevado a la potencia n.

Potencia=int(input("Ingrese la potencia: "))
Valor=2
for i in range(Potencia-1):
    Valor=Valor*2
print(Valor)


#Ejercicio 6
#Leer un numero natural n, leer otro dato de tipo real x y calcular xn

Numero=int(input("Ingrese un numero natural:"))
Numero2=float(input("Ingerse otro numero:"))
print (Numero2**Numero)


#Ejercicio 7
for i in range(1, 10):
    print("\nTabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
