nome =input("Digite o nome: ")
idade =int(input("Digite a idade: "))
doenca_infecocontagiosa =input("Suspeita de doença infectocontagiosa? ").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infecocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infecocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infecocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infecocontagiosa=="NAO":
        print("Encaminhe paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")