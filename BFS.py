from collections import deque

def encontrar_camino(laberinto, entrada, salida):
    fila, columna = len(laberinto), len(laberinto[0])
    visitados = set()
    cola = deque([entrada])
    padres = {}

    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while cola:
        i_actual, j_actual = cola.popleft()
        if (i_actual, j_actual) == salida:
            # Reconstruir el camino desde la salida hasta la entrada
            camino = []
            nodo_actual = salida
            while nodo_actual != entrada:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            camino.append(entrada)
            camino.reverse()
            return camino

        for i_siguiente, j_siguiente in movimientos:
            nodo_siguiente = (i_actual + i_siguiente, j_actual + j_siguiente)
            if 0 <= nodo_siguiente[0] < fila and 0 <= nodo_siguiente[1] < columna:
                if laberinto[nodo_siguiente[0]][nodo_siguiente[1]] == 0 and nodo_siguiente not in visitados:
                    visitados.add(nodo_siguiente)
                    padres[nodo_siguiente] = (i_actual, j_actual)
                    cola.append(nodo_siguiente)

    return None

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
entrada = (0, 0)
salida = (4, 4)

camino = encontrar_camino(laberinto, entrada, salida)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino válido.")
