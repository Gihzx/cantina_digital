from fila import adicionar_pedido, proximo_pedido
from dicionario import (
    adicionar_pedido as cadastrar_pedido,
    buscar_pedido,
    atualizar_status
)

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

    cadastrar_pedido(pedidos, numero_pedido, {
    "aluno": nome,
    "lanche": lanche,
    "bebida": bebida,
    "status": "Aguardando preparacao"
    })

    # Adicionando na fila

    adicionar_pedido(fila, numero_pedido)

    print("\n===== PEDIDO REALIZADO =====")
    print(f"Numero do pedido: {numero_pedido:03d}")
    print(f"Aluno: {nome}")
    print(f"Lanche: {lanche}")
    print(f"Bebida: {bebida}")
    print("Status: Aguardando preparacao")

    return contador_pedidos + 1

def preparar_pedido(pedidos, fila):

    print("\n===== PREPARAR PEDIDO =====")

    numero_pedido = proximo_pedido(fila)

    if numero_pedido is None:
        print("Nao existem pedidos aguardando preparacao!")
        return

    pedido = buscar_pedido(pedidos, numero_pedido)

    if pedido is None:
        print("Pedido nao encontrado!")
        return

    if pedido["status"] != "Aguardando preparacao":
        print("Pedido nao esta aguardando preparacao!")
        return

    atualizar_status(pedidos, numero_pedido, "Em preparacao")

    print(f"Pedido {numero_pedido:03d} encaminhado para preparacao!")

    

def disponibilizar_pedido(pedidos):

    print("\n===== PEDIDO PRONTO =====")

    numero = input("Digite o numero do pedido: ")

    if not numero.isdigit():
        print("Numero invalido!")
        return

    numero = int(numero)

    pedido = buscar_pedido(pedidos, numero)

    if pedido is None:
        print("Pedido nao encontrado!")
        return

    if pedido["status"] != "Em preparacao":
        print("Pedido nao esta em preparacao!")
        return

    atualizar_status(
        pedidos,
        numero,
        "Disponivel para retirada"
    )

    print(f"Pedido {numero:03d} disponivel para retirada!") 
def cancelar_pedido(pedidos):

    print("\n===== CANCELAR PEDIDO =====")

    numero = input("Digite o numero do pedido: ")

    if not numero.isdigit():
        print("Numero invalido!")
        return

    numero = int(numero)

    pedido = buscar_pedido(pedidos, numero)

    if pedido is None:
        print("Pedido nao encontrado!")
        return

    if pedido["status"] in ["Retirado", "Cancelado"]:
        print("Este pedido nao pode ser cancelado!")
        return

    atualizar_status(pedidos, numero, "Cancelado")

    print(f"Pedido {numero:03d} cancelado com sucesso!")

def retirar_pedido(pedidos):

    print("\n===== RETIRAR PEDIDO =====")

    numero = input("Digite o numero do pedido: ")

    if not numero.isdigit():
        print("Numero invalido!")
        return

    numero = int(numero)

    pedido = buscar_pedido(pedidos, numero)

    if pedido is None:
        print("Pedido nao encontrado!")
        return

    if pedido["status"] != "Disponivel para retirada":
        print("Pedido ainda nao esta disponivel para retirada!")
        return

    atualizar_status(pedidos, numero, "Retirado")

    print(f"Pedido {numero:03d} retirado com sucesso!")

def alterar_status(pedidos):


    print("\n===== ATUALIZAR STATUS =====")

    numero = input("Digite o numero do pedido: ")

    if not numero.isdigit():
        print("Numero invalido!")
        return

    numero = int(numero)

    pedido = buscar_pedido(pedidos, numero)

    if pedido is None:
        print("Pedido nao encontrado!")
        return

    print("\nEscolha o novo status:")
    print("1 - Aguardando preparacao")
    print("2 - Em preparacao")
    print("3 - Disponivel para retirada")
    print("4 - Retirado")
    print("5 - Cancelado")

    opcao = input("Digite a opcao: ")

    status = {
        "1": "Aguardando preparacao",
        "2": "Em preparacao",
        "3": "Disponivel para retirada",
        "4": "Retirado",
        "5": "Cancelado"
    }

    if opcao not in status:
        print("Opcao invalida!")
        return

    resultado = atualizar_status(
        pedidos, numero, status[opcao]
    )

    if resultado:
        print("Status atualizado com sucesso!")


def consultar_pedido(pedidos):

    print("\n===== CONSULTAR PEDIDO =====")

    numero = input("Digite o numero do pedido: ")

    if not numero.isdigit():
        print("Numero de pedido invalido!")
        return

    numero = int(numero)

    pedido = buscar_pedido(pedidos, numero)

    if pedido is None:
        print("Pedido nao encontrado!")
        return

    print("\n===== DADOS DO PEDIDO =====")
    print(f"Aluno: {pedido['aluno']}")
    print(f"Lanche: {pedido['lanche']}")
    print(f"Bebida: {pedido['bebida']}")
    print(f"Status: {pedido['status']}")


pedidos = {}
fila = []
contador_pedidos = 1

while True:

    print("\n===== MENU CANTINA DIGITAL =====")
    print("1 - Fazer pedido")
    print("2 - Consultar pedido")
    print("3 - Atualizar status")
    print("4 - Preparar pedido")
    print("5 - Disponibilizar pedido para retirada")
    print("6 - Retirar pedido")
    print("7 - Cancelar pedido")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        contador_pedidos = fazer_pedido(
            pedidos, fila, contador_pedidos
        )

    elif opcao == "2":
        consultar_pedido(pedidos)

    elif opcao == "3":
     alterar_status(pedidos)

    elif opcao == "4":
        preparar_pedido(pedidos, fila)

    elif opcao == "5":
        disponibilizar_pedido(pedidos)

    elif opcao == "6":
      retirar_pedido(pedidos)

    elif opcao == "7":
        cancelar_pedido(pedidos)
        
    elif opcao == "0":
        print("Encerrando sistema...")
    
        break

    else:
        print("Opcao invalida!")

print("\n===== RESUMO DOS PEDIDOS =====")
print("Fila de pedidos:", fila)
print("Pedidos cadastrados:", pedidos)

