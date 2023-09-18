lista = [10, 2, 5, 7, 6, 3]
size = len(lista)

soma = 0

for num in range(size):
    if lista[num] % 2 == 0:
        soma += lista[num]

print(soma)
