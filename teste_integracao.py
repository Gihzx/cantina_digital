from fila import adicionar_pedido, proximo_pedido, consultar_fila
from dicionario import adicionar_pedido as cadastrar_pedido, buscar_pedido, listar_pedidos
from organizacao_pedidos import organizar_pedidos

# Criando o dicionario de pedidos
pedidos = {}

# Cadastrando dois pedidos
cadastrar_pedido(pedidos, 1, {
    "aluno": "Joao",
    "lanche": "Coxinha",
    "bebida": "Suco"
})

cadastrar_pedido(pedidos, 2, {
    "aluno": "Maria",
    "lanche": "Pastel",
    "bebida": "Agua"
})

# Adicionando os pedidos na fila
adicionar_pedido(1)
adicionar_pedido(2)

# Consultando a fila
print("Fila de pedidos:", consultar_fila())

# Consultando um pedido no dicionario
print("Pedido 1:", buscar_pedido(pedidos, 1))

# Organizando os pedidos
print("Pedidos organizados:", organizar_pedidos(pedidos))

# Retirando o proximo pedido
print("Proximo pedido:", proximo_pedido())

print("Fila atualizada:", consultar_fila())