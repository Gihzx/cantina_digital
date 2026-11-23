def adicionar_pedido(pedidos, numero_pedido, dados):
    pedidos[numero_pedido] = dados


def buscar_pedido(pedidos, numero_pedido):
    return pedidos.get(numero_pedido)


def listar_pedidos(pedidos):
    return pedidos.items()