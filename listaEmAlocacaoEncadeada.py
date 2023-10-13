class No:    
	def __init__(self,chave,valor):        
		self.chave =chave
		self.valor = valor        
		self.proximo = None


class ListaEncadeada:
    def __init__(self,cabeca=None):
        self.cabeca = cabeca 
    def print(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo
    def busca(self, k):
        noAtual=self.cabeca
        if noAtual.chave==k:
            return noAtual                #chave encontrada
        while noAtual.proximo != None:
            noAtual=noAtual.proximo       #passe para próximo nó
        if noAtual.chave==k:
            return noAtual             #chave encontrada
        return None                        #indica chave não achada
    def insereFinal(self, novoNo):
        noAtual = self.cabeca
        if noAtual:                     			    #caso a lista nao esteja vazia
            while noAtual.proximo:
                noAtual = noAtual.proximo   	        #busca o final da lista
            noAtual.proximo = novoNo
        else:                           			    #caso a lista esteja vazia
            self.cabeca = novoNo
    def insereInicio(self, novoNo):
        novoNo.proximo = self.cabeca
        self.cabeca=novoNo
    def insereOrdenada (self, novoNo):
        noAtual=self.cabeca				        	   	     #inicio da busca da posição
        if noAtual.chave> novoNo.chave:
            novoNo.proximo = self.cabeca
            self.cabeca=novoNo        		  	  	  	  	     #insere no inicio
            return 0
        if noAtual.proximo!= None:
            while (noAtual.chave< novoNo.chave):
                if (noAtual.proximo==None):
                    noAtual.proximo=novoNo  	 #insere no final
                    return 0
                noAnterior=noAtual
                noAtual=noAtual.proximo	    	  	 #continue a busca
                                                                #fim da busca
        novoNo.proximo=noAtual				  		     	 #apontar novo nó
        noAnterior.proximo= novoNo			 	  		     #inserir novo nó
    def removeLista(self, k):
        noAtual=self.cabeca
        if noAtual==None:          				#erro lista vazia
            return None             
        if noAtual.chave==k:        				#primeiro nó é o alvo
            self.cabeca=noAtual.proximo
            return 0
        noAnterior=noAtual					#continua a busca
        noAtual=noAtual.proximo
        while(noAtual!=None):
            if noAtual.chave==k:                		#chave encontrada
                noAnterior.proximo=noAtual.proximo 	#removeu o nó
                return k
            else:
                noAnterior=noAtual			#continua a busca
                noAtual=noAtual.proximo
        return -1                          			 #erro chave não encontrada


e0=No(0,'Joao')
Lista=ListaEncadeada(e0)
k0=Lista.busca(0)
print(k0.valor)
Lista.print()
e1=No(1,'Maria')
Lista.insereFinal(e1)
Lista.print()
e2=No(-1,'Ana')
Lista.insereInicio(e2)
Lista.print()
e3=No(2,'Arthur')
Lista.insereOrdenada(e3)
Lista.removeLista(2)
Lista.print()
