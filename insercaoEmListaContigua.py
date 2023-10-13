'''
names = ['Igor', 'Ana', 'Maria']
names.append('Carlos')
print(names)

def insereNome(key, list, length):
    list.append('')
    list[length] = key
    return list

novaLista = insereNome('Cleiton', names, len(names))
print(novaLista)
'''

names = ['Ana', 'Aluizio', 'Igor', 'Maria']

def insereOrdenada(chave, lista, tamanhoLista):
    i = 0
    posInsercao = -1
    while i < tamanhoLista:
        if lista[i] >= chave:
            if lista[i] == chave:
                return -1
            else:
                posInsercao = i
                i = tamanhoLista + 1
        else:
            i = i + 1
        if i == tamanhoLista:
            posInsercao = tamanhoLista
    lista.append('')
    i = tamanhoLista
    while (i > posInsercao):
        lista[i] = lista[i - 1]
        i = i - 1
    lista[posInsercao] = chave
    return lista


newlist = insereOrdenada('Beacon', names, len(names))
print(newlist)
