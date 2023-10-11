def replace(seq, index):
    aux = seq[index]
    seq[index] = seq[index + 1]
    seq[index + 1] = aux
    return seq


arrayToSort = [1, 15, 19, 12, 10, 5, 3, 2, 0]
# [1, 15, 22, 6, 7, 19, 8, 3, 5, 20]

troca = 1
while troca:
    troca = 0
    i = 0
    for i in range(len(arrayToSort)-1):
        if arrayToSort[i] > arrayToSort[i + 1]:
            arrayToSort = replace(arrayToSort, i)
            troca = 1

print(arrayToSort)
