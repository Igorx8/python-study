names = ['Igor', 'Ana', 'Alice']
i = names.index('Ana')
print(i)

def buscalista(chave, lista, tamanholista):
    i = 0
    searchindex = -1
    while i < tamanholista:
        if lista[i] == chave:
            searchindex = i
            i = tamanholista + 1
        i = i + 1
    return searchindex

indiceEncontrado = buscalista('Alice', names, len(names))
print(indiceEncontrado)