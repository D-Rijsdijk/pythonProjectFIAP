# Inicializa uma lista vazia chamada "inventario" para armazenar os dados dos equipamentos
inventario = []

# Define a resposta inicial como "S"
resposta = "S"

# Enquanto a resposta for igual a "S", executa o seguinte bloco de código
while resposta == "S":
    # Solicita informações sobre um equipamento ao usuário e armazena em uma lista chamada "equipamento"
    equipamento = [
        input("Equipamento: "),  # Solicita o nome do equipamento
        float(input("Valor: ")),  # Solicita o valor do equipamento (como um número de ponto flutuante)
        int(input("Número Serial: ")),  # Solicita o número serial do equipamento (como um número inteiro)
        input("Departamento: ")  # Solicita o departamento do equipamento
    ]

    # Adiciona a lista "equipamento" à lista "inventario" para armazenamento
    inventario.append(equipamento)

    # Solicita ao usuário se deseja continuar adicionando equipamentos e converte a resposta para maiúsculas
    resposta = input("Digite 'S' para continuar: ").upper()

# Itera sobre cada elemento na lista "inventario" e exibe as informações dos equipamentos
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

# Solicita ao usuário o nome de um equipamento para buscar nas informações
busca = input("Digite o nome do equipamento que deseja buscar: ")

# Procura na lista "inventario" pelo equipamento com o nome especificado e exibe suas informações se encontrado
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

# Solicita ao usuário o nome de um equipamento para aplicar depreciação
depreciacao = input("Digite o nome do equipamento que será depreciado: ")

# Procura na lista "inventario" pelo equipamento com o nome especificado e aplica uma depreciação de 10% ao valor
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9  # Aplica uma depreciação de 10% ao valor
        print("Novo valor: ", elemento[1])

# Solicita ao usuário o número serial de um equipamento para excluí-lo
serial = int(input("Digite o serial do equipamento que será excluído: "))

# Procura na lista "inventario" pelo equipamento com o número serial especificado e o remove da lista
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

# Itera sobre cada elemento restante na lista "inventario" e exibe suas informações atualizadas
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])