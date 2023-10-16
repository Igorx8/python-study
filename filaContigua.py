maxFila=10
fila=[None]*maxFila
inicioFila=None
finalFila=None

class No:    
	def __init__(self,chave,valor):        
		self.chave =chave
		self.valor = valor        
		self.proximo = None



class FilaEncadeada:
	def __init__(self,inicio=None):
			self.inicio = inicio
			self.final =	inicio
	def insere(self, novoNo):
		if self.inicio==None:				#fila vazia
			self.inicio=novoNo			#atualiza o início da fila
			self.final=novoNo			 #atualiza o final da fila
		else:
			self.final.proximo=novoNo		#insere o nó
			self.final =novoNo			      #atualiza o final da fila
	def insereFila(self, novoNo):
		global inicioFila				                 #indica o acesso a variáveis globais
		global maxFila
		global finalFila
		global fila
		if inicioFila== None:				             #fila vazia
					fila[0] = novoNo			             #insere o nó
					inicioFila=0				             #atualiza o início da fila
					
					finalFila=0				             #atualiza o final da fila
		elif (finalFila+1) % maxFila ==inicioFila:	     #fila cheia
				return -1				                 # -1 indica erro de fila cheia
		else:
				finalFila=(finalFila+1) % maxFila	   	 #atualiza o final da fila
				fila[finalFila] = novoNo                 #insere o nó 
		return finalFila				                 #saída normal
	def remove(self):
		if self.inicio==None:				             # erro -fila vazia
					return None			 	         # None indica erro fila vazia
		else:
				k =self.inicio				         #salva o nó removido
				self.inicio=self.inicio.proximo  	 #remove o nó
				return k			                     #retorne k=o nó consumido
	def removeFila(self):
		global inicioFila                 #indica o acesso a variáveis globais
		global maxFila
		global finalFila
		global fila
		if inicioFila== None:                           #fila vazia
			fila.clear()
			return None                            #erro fila vazia
		k=fila[inicioFila]                              #salva o nó removido
		if finalFila==inicioFila:
			inicioFila=None                        #fila vazia após remoção
		else:
			inicioFila=(inicioFila+1) % maxFila    #remove o nó
		return k                                        # retorne k=o nó consumido
	
filaEncadeada = FilaEncadeada()
print(fila)
for i in range(10):
	filaEncadeada.insereFila(i)
	print(fila)
print(filaEncadeada.insereFila(11))
for i in range(10):
	print(filaEncadeada.removeFila())
print(filaEncadeada.removeFila()) 