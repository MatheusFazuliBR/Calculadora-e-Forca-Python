#Agenda Telefonica em Python

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso!")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print("Contato não encontrado.")

    def buscar_contato(self, nome):
        telefone = self.contatos.get(nome)
        if telefone:
            print(f"Contato: {nome}, Telefone: {telefone}")
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):
        for nome, telefone in self.contatos.items():
            print(f"{nome}: {telefone}")

def main():
    agenda = AgendaTelefonica()
    while True:
        print("\nAgenda Telefônica")
        print("1 - Adicionar Contato")
        print("2 - Remover Contato")
        print("3 - Buscar Contato")
        print("4 - Listar Contatos")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Nome do contato a remover: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Nome do contato a buscar: ")
            agenda.buscar_contato(nome)
        elif escolha == '4':
            agenda.listar_contatos()
        elif escolha == '5':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
