import re
import csv

class Usuario:
    def __init__(self, telefone, nome, saldo):
        self.telefone = telefone
        self.nome = nome
        self.saldo = saldo

    def adicionar_creditos(self, valor):
        impressoes = valor * 100 / 30  # Calcula as impressoes baseadas no valor
        self.saldo += impressoes
        print(f"{valor} reais adicionados, equivalente a {impressoes:.0f} impressões. Saldo atual: {self.saldo:.0f} impressões.")

    def debitar_creditos(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"{valor} impressões debitadas. Saldo atual: {self.saldo:.0f} impressões.")
        else:
            print("Saldo insuficiente!")


class SistemaDeImpressao:
    def __init__(self, arquivo_dados="usuarios.csv"):
        self.arquivo_dados = arquivo_dados
        self.usuarios = {}
        self.carregar_usuarios()

    def validar_telefone(self, telefone):
        telefone = telefone.strip()  # Remove espaços extras
        padrao = re.compile(r"^\(\d{3}\)\d{5}-\d{4}$")
        if not padrao.match(telefone):
            print("Telefone inválido. Use o formato (ddd)xxxxx-xxxx.")
            return False
        return True

    def carregar_usuarios(self):
        try:
            with open(self.arquivo_dados, mode="r", newline="") as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pular o cabeçalho
                for linha in leitor:
                    telefone, nome, saldo = linha
                    self.usuarios[telefone] = Usuario(telefone, nome, float(saldo))
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Um novo será criado.")

    def salvar_usuarios(self):
        with open(self.arquivo_dados, mode="w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Telefone", "Nome", "Saldo"])
            for usuario in self.usuarios.values():
                escritor.writerow([usuario.telefone, usuario.nome, usuario.saldo])

    def cadastrar_usuario(self, telefone, nome, saldo_inicial):
        telefone = telefone.strip()  # Remove espaços extras
        if not self.validar_telefone(telefone):
            return

        if telefone in self.usuarios:
            print(f"Usuário com telefone {telefone} já cadastrado.")
        else:
            self.usuarios[telefone] = Usuario(telefone, nome, saldo_inicial * 100 / 30)
            print(f"Usuário {nome} cadastrado com sucesso com saldo equivalente a {saldo_inicial} reais.")
            self.salvar_usuarios()

    def exibir_saldo(self, telefone):
        telefone = telefone.strip()  # Remove espaços extras
        if telefone in self.usuarios:
            print(f"Saldo de {self.usuarios[telefone].nome}: {self.usuarios[telefone].saldo:.0f} impressões.")
        else:
            print("Usuário não encontrado.")

    def adicionar_creditos_usuario(self, telefone, valor):
        telefone = telefone.strip()  # Remove espaços extras
        if telefone in self.usuarios:
            self.usuarios[telefone].adicionar_creditos(valor)
            self.salvar_usuarios()
        else:
            print("Usuário não encontrado.")

    def debitar_creditos_usuario(self, telefone, valor):
        telefone = telefone.strip()  # Remove espaços extras
        if telefone in self.usuarios:
            self.usuarios[telefone].debitar_creditos(valor)
            self.salvar_usuarios()
        else:
            print("Usuário não encontrado.")

    def listar_usuarios(self):
        print("Usuários cadastrados:")
        for usuario in self.usuarios.values():
            print(f"Telefone: {usuario.telefone}, Nome: {usuario.nome}, Saldo: {usuario.saldo:.0f} impressões.")


def main():
    sistema = SistemaDeImpressao()

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar usuário")
        print("2. Exibir saldo")
        print("3. Adicionar créditos")
        print("4. Debitar créditos")
        print("5. Listar usuários")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            telefone = input("Digite o telefone do usuário (formato: (ddd)xxxxx-xxxx): ")
            nome = input("Digite o nome do usuário: ")
            saldo_inicial = float(input("Digite o saldo inicial em reais: "))
            sistema.cadastrar_usuario(telefone, nome, saldo_inicial)

        elif opcao == "2":
            telefone = input("Digite o telefone do usuário: ")
            sistema.exibir_saldo(telefone)

        elif opcao == "3":
            telefone = input("Digite o telefone do usuário: ")
            valor = float(input("Digite o valor em reais a adicionar: "))
            sistema.adicionar_creditos_usuario(telefone, valor)

        elif opcao == "4":
            telefone = input("Digite o telefone do usuário: ")
            valor = float(input("Digite a quantidade de impressões a debitar: "))
            sistema.debitar_creditos_usuario(telefone, valor)

        elif opcao == "5":
            sistema.listar_usuarios()

        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
