# 🍔 CANTINA DIGITAL
### Peça antes, retire no intervalo!

<p align="center">
  <strong>Mais organização, menos filas e muito mais praticidade!</strong>
</p>

---

## 📌 Sobre o projeto

A **Cantina Digital** é um sistema desenvolvido em Python com o objetivo de otimizar a organização dos pedidos realizados em uma cantina escolar.

A proposta surgiu a partir de um problema comum na rotina dos estudantes: as longas filas durante o intervalo, que acabam reduzindo o tempo disponível para alimentação e descanso.

Com o sistema, os pedidos podem ser registrados antecipadamente e organizados de maneira eficiente, permitindo que a cantina acompanhe cada etapa do atendimento.

**A ideia é simples: o aluno pede antes, a cantina prepara e, quando o intervalo chega, é só retirar!**

## 🎯 Objetivo

Desenvolver uma aplicação que utilize conceitos de Estrutura de Dados para organizar e gerenciar pedidos de uma cantina escolar, demonstrando como a programação pode contribuir para solucionar situações do cotidiano.

## ✨ Funcionalidades

O sistema foi planejado para oferecer recursos que facilitam o gerenciamento dos pedidos:

| Funcionalidade | Descrição |
|---|---|
| 📝 Cadastro de pedidos | Registra o nome do aluno e o lanche escolhido. |
| 🔢 Identificação | Gera um número para identificar cada pedido. |
| 🔎 Consulta | Permite localizar pedidos pelo número. |
| 📋 Organização | Organiza os pedidos conforme a ordem de chegada. |
| 👩‍🍳 Preparação | Permite acompanhar o andamento da preparação. |
| 🥡 Retirada | Registra a finalização e retirada dos pedidos. |
| 📊 Relatório | Permite visualizar informações dos pedidos, conforme os recursos implementados. |

## 🔄 Situações dos pedidos

Cada pedido pode passar pelas seguintes etapas:

- 🟡 **Aguardando preparação:** pedido registrado e aguardando atendimento.
- 🔵 **Em preparação:** lanche em processo de preparo.
- 🟢 **Pronto para retirada:** pedido finalizado e disponível para o aluno.
- ⚪ **Retirado:** pedido entregue ao aluno.

## 🧠 Estruturas de Dados

Um dos principais objetivos do projeto é aplicar, na prática, os conceitos estudados na disciplina de Estrutura de Dados.

### 1. Fila – FIFO

A fila é utilizada para organizar os pedidos conforme sua ordem de chegada.

O conceito FIFO (*First In, First Out*) significa que o primeiro elemento inserido é o primeiro a ser removido.

**Exemplo:**

```text
Entrada:
001 → 002 → 003

Ordem de atendimento:
001 → 002 → 003
```

### 2. Dicionário – dict

O dicionário é utilizado para armazenar e organizar as informações dos pedidos por meio de pares de chave e valor.

Exemplo:

```python
pedido = {
    "numero": "001",
    "aluno": "Ana",
    "lanche": "Sanduíche",
    "status": "Aguardando preparação"
}
```

Essa estrutura facilita a consulta e a atualização das informações de cada pedido.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Collections:** biblioteca utilizada para trabalhar com estruturas de dados, como deque.
- **Terminal/Console:** ambiente de execução do sistema.
- **Git e GitHub:** ferramentas utilizadas para organização e compartilhamento do projeto.

## 📂 Organização dos arquivos

O projeto está organizado em módulos para facilitar a manutenção e a integração das funcionalidades.

```text
cantina_digital/
│
├── cadastro.py
├── fila.py
├── dicionario.py
├── organizacao_pedidos.py
├── teste_integracao.py
│
├── README.md
└── README_estruturas.md
```

Cada arquivo possui uma responsabilidade dentro da organização do sistema, contribuindo para uma estrutura de código mais organizada.

## ▶️ Como executar o projeto

### Pré-requisitos

- Python 3 instalado.
- Editor de código ou terminal.
- Arquivos do projeto disponíveis no computador.

### Passo a passo

**1. Clone o repositório:**

```bash
git clone https://github.com/Gihzx/cantina_digital.git
```

**2. Acesse a pasta do projeto:**

```bash
cd cantina_digital
```

**3. Execute o sistema:**

```bash
python cadastro.py
```

Caso seu ambiente utilize o comando `python3`, execute:

```bash
python3 cadastro.py
```

## 🧪 Testes e integração

A etapa de integração e testes tem como objetivo verificar o funcionamento das funcionalidades e a comunicação entre os módulos.

Entre os cenários considerados estão:

- Cadastro de novos pedidos.
- Consulta de pedidos existentes e inexistentes.
- Visualização e organização da fila.
- Preparação dos pedidos.
- Atualização das situações.
- Finalização das retiradas.
- Validação de opções inválidas.
- Encerramento do sistema.

Os testes também permitem identificar possíveis falhas e oportunidades de melhoria.

## 👥 Equipe de desenvolvimento

Projeto desenvolvido por uma equipe de quatro integrantes, com divisão de responsabilidades:

| Integrante | Responsabilidade |
|---|---|
| Integrante 1 | Cadastro e cardápio |
| Integrante 2 | Estruturas de dados |
| Integrante 3 | Gerenciamento dos pedidos |
| Integrante 4 | Integração e testes |

Todos os integrantes participam do desenvolvimento e da compreensão geral do sistema.

## 🎓 Informações acadêmicas

**Projeto:** Cantina Digital – Peça antes, retire no intervalo!

**Disciplina:** Estrutura de Dados

**Linguagem:** Python

**Interface:** Terminal/Console

**Apresentação:** 27 de novembro de 2026

## 💡 Considerações finais

A Cantina Digital demonstra como os conceitos de programação e Estrutura de Dados podem ser aplicados na criação de soluções para problemas reais.

Mais do que organizar pedidos, o projeto proporciona uma experiência prática de desenvolvimento em equipe, integração de módulos e aplicação de estruturas de dados.

Nosso propósito é mostrar que pequenas soluções tecnológicas podem tornar atividades do cotidiano mais simples, organizadas e eficientes.

---

<p align="center">
  **🍔 CANTINA DIGITAL**
  
  *Peça antes. Aproveite melhor o intervalo!*
  
  <strong>Desenvolvido com dedicação pela equipe Cantina Digital. ❤️</strong>
</p>
