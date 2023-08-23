usuarios = {}

# Solicita ação ao usuário e converte para maiúsculas
opcao = input("O que deseja realizar?\n" +
              "<I> - Para Inserir um usuário\n" +
              "<P> - Para Pesquisar um usuário\n" +
              "<E> - Para Excluir um usuário\n" +
              "<L> - Para Listar um usuário: ").upper()

# Continua executando enquanto a opção escolhida for válida
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        usuarios[chave] = [input("Digite o nome: ").upper(),
                           input("Digite a última data de acesso: "),
                           input("Qual a última estação acessada: ").upper()]

    # Solicita ação novamente ao usuário
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar um usuário: ").upper()

# Encerrando o programa caso a opção seja diferente das permitidas
print("Programa encerrado.")