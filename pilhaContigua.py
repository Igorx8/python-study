maxPilha=10
pilha=[None]*maxPilha
topoPilha=None

class PilhaEncadeada:
    def __init__(self,topo=None):
            self.topo = topo
    def push(self,novoNo):
        novoNo.proximo=self.topo    		#insere o nó
        self.topo=novoNo            		#atualiza o topo da pilha
    def pushContigua(self, novoNo):
        global pilha
        global topoPilha
        global maxPilha
        if topoPilha== None:				         #pilha vazia
                pilha[0] = novoNo			         #insere o nó
                topoPilha=0			      	         #atualiza o topo da pilha
        elif topoPilha == maxPilha-1:		         #pilha cheia
                return -1		          		     # -1 → erro de pilha cheia
        else:
                topoPilha=topoPilha+1			     #atualiza o topo da pilha
                pilha[topoPilha] = novoNo	  	     #insere o nó
        return  topoPilha				             #saída normal
    def pop(self):
        if self.topo==None:
           return None             		#erro pilha vazia
        k=self.topo                 	#salva o nó removido
        self.topo=self.topo.proximo 	#remove o nó
        return k                    	#retorna o nó removido
    def popContigua(self):
        global pilha
        global topoPilha
        global maxPilha
        if topoPilha== None: 			       # erro -pilha vazia
            return  None			       # None indica erro pilha vazia
        else:
            k =pilha[topoPilha]	           # salva o nó removido
            if topoPilha==0:
                topoPilha=None	           #pilha vazia após remoção
            else:
                topoPilha=topoPilha-1	   #remove o nó
            return k	                   #retorne k=o nó consumido

pilhaEncadeada = PilhaEncadeada()
print(pilha)
for i in range(10):
    pilhaEncadeada.pushContigua(i)  
    print(pilha)    
print(pilhaEncadeada.pushContigua(11))
for i in range(10):
    print(pilhaEncadeada.popContigua())
print(pilhaEncadeada.popContigua())