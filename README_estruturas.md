# Estruturas de Dados — Cantina Digital

Este documento apresenta as estruturas de dados implementadas para o projeto Cantina Digital.

## 1. Fila de pedidos — fila.py

Utiliza `deque`, da biblioteca `collections`, para controlar a ordem de atendimento dos pedidos.

Funções disponíveis:

- `adicionar_pedido(numero_pedido)`: adiciona um pedido ao final da fila.
- `proximo_pedido()`: retira e retorna o primeiro pedido da fila. Retorna `None` se estiver vazia.
- `consultar_fila()`: retorna os pedidos que ainda estão na fila.

A fila segue a regra FIFO (First In, First Out): o primeiro pedido a entrar é o primeiro a sair.

## 2. Dicionário de pedidos — dicionario.py

Utiliza um dicionário Python para armazenar e consultar os pedidos.

Funções disponíveis:

- `adicionar_pedido(pedidos, numero_pedido, dados)`: adiciona um pedido ao dicionário.
- `buscar_pedido(pedidos, numero_pedido)`: procura um pedido pelo número.
- `listar_pedidos(pedidos)`: retorna os pedidos cadastrados.

## 3. Organização dos pedidos — organizacao_pedidos.py

Organiza os pedidos pelo número em ordem crescente.

Função disponível:

- `organizar_pedidos(pedidos)`: retorna os pedidos organizados pelo número.

## 4. Testes

O arquivo `teste_integracao.py` foi utilizado para testar o funcionamento conjunto das três estruturas.

Os testes verificaram a inserção, consulta, organização e retirada dos pedidos.

## 5. Observação

Os módulos foram desenvolvidos separadamente para facilitar sua utilização e integração ao restante do sistema.