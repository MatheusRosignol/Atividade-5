numeros = []  # lista vazia para armazenar os números digitados

# loop para a leitura dos números
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

soma = 0  # variável para armazenar a soma dos números

# loop para a soma dos números
for num in numeros:
    soma += num

print("A soma dos números digitados é:", soma)