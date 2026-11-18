print("\n=======================================")
print("\n         CANTINA DIGITAL               ")
print("\n    Peça Antes, Retire no Intervalo!   ")
print("\n=======================================")
# Cardapio de lanches

lanches = {
    1: "Sanduiche",
    2: "Pao de Queijo",
    3: "Coxinha",
    4: "Pastel"
}


# Cardapio de bebidas

bebidas = {
    1: "Suco",
    2: "Achocolatado",
    3: "Agua",
    4: "Refrigerante"
}


# Funcao para mostrar os cardapios

def mostrar_cardapio():

    print("\n============ LANCHES ===========")

    for numero, lanche in lanches.items():
        print(f"{numero} - {lanche}")

    print("\n============ BEBIDAS ============")

    for numero, bebida in bebidas.items():
        print(f"{numero} - {bebida}")


# Funcao para fazer o pedido

def fazer_pedido(pedidos, fila, contador_pedidos):

    print("\n============ NOVO PEDIDO ============")

    nome = input("Digite o nome do aluno: ").strip()

    if nome == "":
        print("Nome invalido!")
        return contador_pedidos

    mostrar_cardapio()

    # Escolha do lanche

    escolha_lanche = input("\nEscolha o numero do lanche: ")

    if not escolha_lanche.isdigit():
        print("Opcao de lanche invalida!")
        return contador_pedidos

    escolha_lanche = int(escolha_lanche)

    if escolha_lanche not in lanches:
        print("Lanche nao encontrado!")
        return contador_pedidos

    # Escolha da bebida

    escolha_bebida = input("Escolha o numero da bebida: ")

    if not escolha_bebida.isdigit():
        print("Opcao de bebida invalida!")
        return contador_pedidos

    escolha_bebida = int(escolha_bebida)

    if escolha_bebida not in bebidas:
        print("Bebida nao encontrada!")
        return contador_pedidos

    # Recuperando os nomes escolhidos

    lanche = lanches[escolha_lanche]
    bebida = bebidas[escolha_bebida]

    # Gerando numero do pedido

    numero_pedido = contador_pedidos

    # Armazenando as informacoes

    pedidos[numero_pedido] = {
        "aluno": nome,
        "lanche": lanche,
        "bebida": bebida,
        "status": "Aguardando preparacao"
    }

    # Adicionando na fila

    fila.append(numero_pedido)

    print("\n===== PEDIDO REALIZADO =====")
    print(f"Numero do pedido: {numero_pedido:03d}")
    print(f"Aluno: {nome}")
    print(f"Lanche: {lanche}")
    print(f"Bebida: {bebida}")
    print("Status: Aguardando preparacao")

    return contador_pedidos + 1
