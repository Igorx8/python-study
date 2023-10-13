'''
nomes= ['Joao','Maria','Ana']
i=nomes.index('Joao')         #busca o índice do nó com a chave Joao
print(i)
'''


names = ['Igor', 'Mariana', 'Marina', 'Neide', 'Ana', 'Julia']

def searchIndex(key, list, lenght):
    i = 0
    indexFound = -1
    while i < lenght:
        if list[i] == key:
            indexFound = i
            i = lenght + 1
        else:
            i = i + 1
    
    return indexFound

nameIndex = searchIndex('Cleiton', names, len(names))
print(nameIndex)

numeros=[1,2,3,4,6,7,8,9,10]
first=searchIndex(5,numeros,len(numeros))
print (first)
second=searchIndex(3,numeros,len(numeros))
print(second)