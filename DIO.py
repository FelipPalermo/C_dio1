from datetime import datetime
from math import floor


class Conta:

    def __init__(self, NomeCliente, TipoConta, TipoCliente, DataAbertura):
        self.NomeCliente = NomeCliente
        self.TipoConta = TipoConta
        self.TipoCliente = TipoCliente
        self.DataAbertura = DataAbertura
        self.saldo = 0

    def Depositar(self, valor) -> None:
        self.saldo += valor
        print(
            f"Desposito efetuado com sucesso.\nR${valor} adicionado a sua conta!"
        )

    def Sacar(self, valor) -> None:
        if self.saldo - valor < 0:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(
                f"Saque efetuado com sucesso.\nR${valor} removido da sua conta!"
            )

    def CalcularValorTarifaManutencao(self) -> int:
        tarifa = floor(float(self.saldo * 0.10) + 5)
        print(f"Tarifa atual : R${tarifa}")


class Conta_Corrente(Conta):
    def __init__(self, NomeCliente, TipoConta, TipoCliente, DataAbertura):
        super().__init__(NomeCliente, TipoConta, TipoCliente, DataAbertura)


class Conta_Investimento(Conta):
    def __init__(self, NomeCliente, TipoConta, TipoCliente, DataAbertura):
        super().__init__(NomeCliente, TipoConta, TipoCliente, DataAbertura)


class Cliente:
    def __init__(self, Nome):
        self.Nome = Nome
        self.contas = []

    def Adicionar_contas(self, conta) -> None:
        for contas in conta:
            self.contas.append(contas)

    def Somar_saldos(self) -> None:
        saldo_total = sum(conta.saldo for conta in self.contas)
        print(f"O saldo de todas as contas : R${saldo_total}.")


felipe = Cliente("Felipe")
f_corrente = Conta_Corrente("Felipe", "Corrente", "Normal", datetime.now())
f_investimento = Conta_Investimento(
    "Felipe", "Investimento", "Normal", datetime.now()
)

felipe.Adicionar_contas([f_corrente, f_investimento])

f_investimento.Depositar(5000)
f_corrente.Depositar(25000)

felipe.Somar_saldos()
