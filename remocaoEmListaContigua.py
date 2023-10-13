names = ['Renan', 'Carlinhos', 'Bruna', 'Alma', 'Cleiton', 'Rasta']
'''
names.remove('Carlinhos')
print(names)
names.pop(0)
print(names)
'''

def removeone(key, list, lenght):
    i = 0
    removePos = -1
    while i < lenght:
        if list[i] == key:
            removePos = i
            i = lenght + 1
        else:
            i = i + 1
    if i == lenght:
        return -1
    i = removePos
    while i < lenght -1:
        list[i] = list[i + 1]
        i = i + 1
    list.pop(lenght - 1)
    return list

removedPos = removeone('Alma', names, len(names))
print(removedPos)