'''
amigos =[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário']]
amigos.append(['Thiago',30,'Capricórnio'])
print(amigos)

amigos =[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário']]
amigos.remove(['João',25,'Câncer'])
print(amigos)

amigos =[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário']]
amigos[2].remove(31)
print(amigos)

amigos =[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário']]
amigos.pop(0)
amigos[1].pop(1)
print(amigos)

amigos =[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário']]
for x in amigos:
    print(x)


amigos =[['João',25, 'Câncer'], ['Maria', 23,'Áries'], ['Ana', 31, 'Aquário']]
for x in amigos:
    for y in x:
        print(y)

amigos =[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário'], ['Mário']]
for x in amigos:
    for y in x:
        print(y)

amigos=[['João',25,'Câncer'], ['Maria',23,'Áries'], ['Ana',31,'Aquário'], ['Mário']]
for x in amigos:
	if isinstance (x,list):
		for y in x:
			print(y)
	else:
		print(x)

import numpy as np
matriz1=np.array([[1,2],[3,4],[5,6]])
matriz2=np.array([[7,8],[9,10],[11,12]])
matriz2=matriz1+matriz2
print(matriz2)
matriz2=matriz2-matriz1
print(matriz2)

'''

import numpy as np  
matriz=np.array([[1,2],[3,4],[5,6]])
minimo = matriz.min()
maximo= matriz.max()
soma=matriz.sum()
media=matriz.mean()
desvio=matriz.std()
print("Minimo =", minimo)
print("Maximo =", maximo)
print("Soma =", soma)
print("Media =", media)
print("Desvio =", desvio)