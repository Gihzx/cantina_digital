

def adicionar_pedido(pedidos, numero_pedido, dados):
    pedidos[numero_pedido] = dados


def buscar_pedido(pedidos, numero_pedido):
    return pedidos.get(numero_pedido)


def atualizar_status(pedidos, numero_pedido, novo_status):

    pedido = buscar_pedido(pedidos, numero_pedido)

    if pedido is None:
        return False

    pedido["status"] = novo_status

    return True

def listar_pedidos(pedidos):
    return pedidos.items()