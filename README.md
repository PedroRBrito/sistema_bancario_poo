# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python utilizando o paradigma de Programação Orientada a Objetos (POO). O sistema permite cadastrar clientes, criar contas bancárias, realizar saques, depósitos e consultar extratos.

## Funcionalidades

- Cadastro de clientes com CPF único
- Criação automática de conta para o cliente
- Login por CPF
- Operações bancárias:
  - Saque (limite de R$500,00 por vez)
  - Depósito
  - Consulta de extrato
- Listagem de clientes cadastrados no banco

## Estrutura do Projeto

O sistema é composto por três classes principais:

### Classe `Cliente`

Representa um cliente do banco.

**Atributos:**
- `_nome`: Nome do cliente
- `_cpf`: CPF do cliente (chave única)
- `_contas`: Lista de contas associadas ao cliente

**Métodos:**
- `nome_cliente()`: Retorna o nome do cliente
- `adicionar_conta(conta)`: Associa uma conta ao cliente
- `listar_contas()`: Retorna a primeira conta associada ao cliente

### Classe `Conta`

Representa uma conta bancária.

**Atributos:**
- `_cliente`: Cliente dono da conta
- `_nro_conta`: Número da conta
- `_agencia`: Número da agência (padrão: "0001")
- `_saldo`: Saldo da conta
- `_historico`: Lista de transações

**Métodos:**
- `obter_nome_cliente()`: Retorna o nome do cliente da conta
- `obter_nro_conta()`: Retorna o número da conta
- `obter_nro_agencia()`: Retorna o número da agência
- `saldo_conta()`: Retorna o saldo da conta
- `saque(valor)`: Realiza um saque (limite de R$500,00 por transação)
- `deposito(valor)`: Realiza um depósito
- `extrato()`: Exibe o histórico de transações

### Classe `Banco`

Gerencia os clientes e contas do sistema.

**Atributos:**
- `_clientes`: Dicionário com os clientes cadastrados (chave: CPF)
- `_nro_conta`: Contador de números de conta

**Métodos:**
- `cadastrar_cliente()`: Cadastra um novo cliente e cria uma conta
- `login(cpf)`: Busca um cliente pelo CPF
- `lista_clientes_banco()`: Retorna todos os clientes cadastrados

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/PedroRBrito/sistema_bancario_poo.git