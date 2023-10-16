from collections import deque

q=deque()			     #cria o deque
q.append('b')		     #insere no final
q.append('c')
q.appendleft('a')
print(q)			     #imprime o deque
print(q.popleft())	     #remove do inicio
print(q.pop())	     	 #remove do final


# Deque é uma estrutura de dados que permite a inserção e remoção de elementos em ambas as extremidades da estrutura. Como uma mistura entre fila e pilha.