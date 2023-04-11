import numpy as np

dieimes_matriz = np.array([[3, 4, 1], [3, 1, 2]])

soma = 0  # variável para armazenar a soma dos elementos da matriz

# loop para percorrer cada linha da matriz
for linha in dieimes_matriz:
    # loop interno para percorrer cada elemento da linha
    for elemento in linha:
        soma += elemento

print("A soma de todos os elementos da matriz é:", soma)