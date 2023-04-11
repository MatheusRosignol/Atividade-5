alunos = {}  # dicionário vazio para armazenar os dados dos alunos

# loop para a leitura dos dados dos alunos
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

soma_notas = 0  # variável para armazenar a soma das notas

# loop para a soma das notas
for nota in alunos.values():
    soma_notas += nota

media = soma_notas / len(alunos)  # cálculo da média

print("A média das notas é:", media)