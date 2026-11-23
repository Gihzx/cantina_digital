
def adicionar_pedido(fila, numero_pedido):
    fila.append(numero_pedido)


def proximo_pedido(fila):
    if len(fila) > 0:
        return fila.pop(0)
    return None


def consultar_fila(fila):
    return fila
