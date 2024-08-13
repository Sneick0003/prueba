import random  # Importa el módulo random para generar números aleatorios

# Función para crear la matriz del tablero y colocar minas
def crea_Matriz_Bool(A, filas, columnas, minas):
    # Inicializa la matriz con ceros
    for i in range(filas):
        c = []
        for j in range(columnas):
            c.append(0)
        A.append(c)

    # Coloca minas aleatoriamente en la matriz
    k = 1
    while k <= minas:
        x = random.randint(0, filas - 1)
        y = random.randint(0, columnas - 1)
        if A[x][y] == 0:
            A[x][y] = "*"
            k += 1

# Función para imprimir la matriz de juego
def Imprimir(A):
    print(" ", end=" ")
    # Imprime los números de columna
    for i in range(len(A[0])):
        print(i, end=" ")
    print()
    # Imprime cada fila de la matriz
    for i in range(len(A)):
        print(i, end="|")
        for j in A[i]:
            print(j, end=" ")
        print()

# Función para verificar y contar las minas alrededor de cada celda
def Verifica(A, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            if A[i][j] != "*":  # Solo se verifica si la celda no contiene una mina
                for x in range(max(0, i - 1), min(filas, i + 2)):
                    for y in range(max(0, j - 1), min(columnas, j + 2)):
                        if A[x][y] == "*":
                            A[i][j] += 1
            if A[i][j] == 0:
                A[i][j] = " "  # Las celdas sin minas alrededor se marcan con un espacio

# Función para crear la matriz visible al jugador durante el juego
def Matriz_juego(B, filas, columnas):
    for i in range(filas):
        c = []
        for j in range(columnas):
            c.append("#")  # Inicializa la matriz con '#' representando celdas ocultas
        B.append(c)

# Función para crear una copia de la matriz original para mostrar al final del juego
def Matrizfinal(A, C, filas, columnas):
    for i in range(filas):
        d = []
        for j in range(columnas):
            d.append(A[i][j])
        C.append(d)

# Función para manejar la jugada del jugador
def Jugada(A, B, C, x, y, filas, columnas):
    global k, n
    if A[x][y] != "*" and A[x][y] != False:
        B[x][y] = A[x][y]  # Muestra el valor de la celda en la matriz de juego

        if A[x][y] == " ":
            A[x][y] = 0 
            for i in range(max(0, x - 1), min(filas, x + 2)):
                for j in range(max(0, y - 1), min(columnas, y + 2)):
                    if A[i][j] == " ":
                        Jugada(A, B, C, i, j, filas, columnas)  # Descubre las celdas. 
        else:
            n += 1
            A[x][y] = False
    elif A[x][y] == "*":
        k = False
        print("\n", "Perdiste".center(50, "-"), "\n")
        Imprimir(C)  # Muestra la matriz completa al perder

# Función principal que controla el flujo del juego
def main():
    v = True
    while v:
        filas = int(input("Ingresa el número de filas: "))
        columnas = int(input("Ingresa el número de columnas: "))
        minas = int(input("Ingresa el número de minas: "))

        global k, n
        k = True
        n = 0

        A = []
        B = []
        C = []

        crea_Matriz_Bool(A, filas, columnas, minas)
        Verifica(A, filas, columnas)
        Matrizfinal(A, C, filas, columnas)
        Matriz_juego(B, filas, columnas)

        while k and n < (filas * columnas - minas):
            Imprimir(B)
            x = int(input("Ingrese el valor de x: "))
            y = int(input("Ingrese el valor de y: "))
            if x >= filas or y >= columnas:
                print("La jugada excede los límites del tablero")
            else:
                if A[x][y] == 0:
                    print("La jugada ya fue realizada")
                else:
                    Jugada(A, B, C, x, y, filas, columnas)
                    print()
        if n == (filas * columnas - minas):
            g = "Ganaste"
            print("\n", g.center(50, "="), "\n")
            Imprimir(B)

        print("Si desea volver a jugar, coloque 1. De lo contrario, coloque 0")
        nuevo_juego = int(input())
        if nuevo_juego == 0:
            v = False

# Llama a la función principal
if __name__ == "__main__":
    main()
