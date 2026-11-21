from collections import deque

fila = deque()

def adicionar_pedido(numero_pedido):
    fila.append(numero_pedido)


def proximo_pedido():
    if len(fila) > 0:
        return fila.popleft()

    return None


def consultar_fila():
    return list(fila)