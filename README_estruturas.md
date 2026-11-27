# Estruturas de Dados — Cantina Digital

Este documento apresenta as estruturas de dados utilizadas no desenvolvimento do projeto Cantina Digital, explicando suas funcionalidades e sua contribuição para o funcionamento do sistema.

## 1. Fila de pedidos — `fila.py`

Utiliza uma lista (`list`) do Python para controlar a ordem de atendimento dos pedidos.

**Funções disponíveis:**

- `adicionar_pedido(numero_pedido)`: adiciona um pedido ao final da fila.
- `proximo_pedido()`: remove e retorna o primeiro pedido da fila. Caso esteja vazia, retorna `None`.
- `consultar_fila()`: retorna os pedidos que ainda estão aguardando atendimento.

A fila segue a regra **FIFO (First In, First Out)**, ou seja, o primeiro pedido a entrar é o primeiro a sair. Essa estrutura permite manter uma sequência organizada de atendimento, garantindo que os pedidos sejam processados na ordem de chegada.

## 2. Dicionário de pedidos — `dicionario.py`

Utiliza um dicionário Python (`dict`) para armazenar e consultar os pedidos cadastrados, utilizando o número do pedido como identificador.

**Funções disponíveis:**

- `adicionar_pedido(pedidos, numero_pedido, dados)`: adiciona um pedido ao dicionário.
- `buscar_pedido(pedidos, numero_pedido)`: procura um pedido pelo número informado.
- `listar_pedidos(pedidos)`: retorna os pedidos cadastrados.

O dicionário facilita o armazenamento e a recuperação das informações dos pedidos, permitindo localizar rapidamente um registro por meio de seu número identificador.

## 3. Organização dos pedidos — `organizacao_pedidos.py`

Responsável por organizar os pedidos de acordo com seus números, em ordem crescente.

**Função disponível:**

- `organizar_pedidos(pedidos)`: retorna os pedidos organizados pelo número.

Essa funcionalidade facilita a visualização e a conferência dos pedidos cadastrados, contribuindo para a organização das informações do sistema.

## 4. Testes de integração — `teste_integracao.py`

O arquivo `teste_integracao.py` foi desenvolvido para testar o funcionamento conjunto dos módulos do projeto.

Os testes contemplam operações de inserção, consulta, organização e retirada de pedidos, permitindo verificar a interação entre as estruturas de dados utilizadas.

## 5. Organização dos módulos

Os módulos foram desenvolvidos separadamente, cada um com uma responsabilidade específica, facilitando a manutenção, a reutilização das funções e a integração ao restante do sistema.

A utilização da fila e do dicionário permite organizar o fluxo de atendimento e armazenar as informações dos pedidos, contribuindo para o funcionamento da proposta da Cantina Digital.
