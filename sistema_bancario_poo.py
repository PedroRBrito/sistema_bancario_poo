class Cliente:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._contas = []

    def nome_cliente(self):
        return self._nome

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        if self._contas:
            return self._contas[0]
        return None

    def __str__(self):
        return f"Cliente: {self._nome}"


class Conta:
    def __init__(self, cliente, nro_conta, agencia="0001", saldo=0):
        self._cliente = cliente
        self._nro_conta = nro_conta
        self._agencia = agencia
        self._saldo = saldo
        self._historico = []

    def obter_nome_cliente(self):
        return self._cliente.nome_cliente()

    def obter_nro_conta(self):
        return self._nro_conta

    def obter_nro_agencia(self):
        return self._agencia

    def saldo_conta(self):
        return self._saldo

    def saque(self, valor):
        if self._saldo == 0:
            return "Sem saldo disponível!"

        elif valor > 500:
            return "Limite do valor do saque de R$500,00"

        elif valor <= 0:
            return "Valor inválido!"

        else:
            self._saldo -= valor
            self._historico.append(f"Saque: {valor:0.2f}")
            return f"Saque de R${valor:0.2f} realizado com sucesso!"

    def deposito(self, valor):
        self._saldo += valor
        self._historico.append(f"Deposito: {valor:0.2f}")
        return f"Deposito de R${valor:0.2f} realizado com sucesso!"

    def extrato(self):
        print("--------Extrato--------")
        for e in self._historico:
            print(e)
        return "-----------------------"

    def __str__(self):
        return f"Conta: {self._nro_conta}\nAgência: {self._agencia}"


class Banco:
    def __init__(self):
        self._clientes = {}
        self._nro_conta = 1

    def cadastrar_cliente(self):
        nome = input("Informe seu nome: ")
        cpf = input("Informe seu CPF: ")

        if cpf in self._clientes:
            return "CPF já cadastrado!"

        cliente = Cliente(nome, cpf)
        conta = Conta(cliente, self._nro_conta, saldo=0)
        cliente.adicionar_conta(conta)

        self._clientes[cpf] = cliente
        self._nro_conta += 1

        return f"Cliente {nome} cadastrado com sucesso! Conta criada!"

    def login(self, cpf):
        if cpf in self._clientes:
            return self._clientes[cpf]
        else:
            print("Cliente não encontrado!")
            msg_criacao_conta = self.cadastrar_cliente()
            print(msg_criacao_conta)

        return None

    def lista_clientes_banco(self):
        return self._clientes


def menu_conta(conta):
    nome = conta.obter_nome_cliente()
    saldo = conta.saldo_conta()
    return (
        input(
            f"""
----------Informações---------
Cliente: {nome}
Saldo : {saldo:0.2f}

-------------Menu--------------
[S] Saque                         |
[D] Depósito                      |
[E] Extrato                       |
[T] Trocar de conta ou sair       |
-------------------------------

""").strip().lower())


def tela_login():

    return (
        input(
            """
-------------Login------------

Digite seu CPF:

------------------------------

""").strip().lower())


def menu_inicial():
    return (
        input("""
-----------Bem-Vindo----------
Qual das opções quer seguir?

[L] Login
[C] Listar clientes
[S] Sair
------------------------------

""").strip().lower())


def lista_de_clientes():
    print("-------------Lista de contas------------")
    if banco.lista_clientes_banco():
        for cliente in banco.lista_clientes_banco().values():
            conta = cliente.listar_contas()
            nome = conta.obter_nome_cliente()
            agencia = conta.obter_nro_agencia()
            n_conta = conta.obter_nro_conta()
            print(
                f"""
Nome: {nome}
Agência: {agencia}
Conta: {n_conta}

----------------------------------------"""
            )
    else:
        print("Não existem clientes no banco!")


banco = Banco()

while True:
    inicio = menu_inicial()

    if inicio == "l":
        cpf = tela_login()
        cliente_logado = banco.login(cpf)
        if cliente_logado:
            conta = cliente_logado.listar_contas()

            while True:
                saldo = conta.saldo_conta()
                opcao_conta = menu_conta(conta)

                if opcao_conta == "s":
                    valor = float(input("Digite o valor do saque: "))
                    print(conta.saque(valor))

                elif opcao_conta == "d":
                    valor = float(input("Digite o valor do deposito: "))
                    print(conta.deposito(valor))

                elif opcao_conta == "e":
                    print(conta.extrato())

                elif opcao_conta == "t":
                    break

                else:
                    print("Opção inválida!")

    elif inicio == "c":
        lista_contas = lista_de_clientes()

    elif inicio == "s":
        break
