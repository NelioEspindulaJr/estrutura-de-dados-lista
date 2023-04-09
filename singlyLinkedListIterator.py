from doublyLinkedListIterator import DoublyLinkedListIterator

class ListNode:
    """
    A classe ListNode define um nó da lista, que armazena dois campos: highway, 
    que guarda um valor associado ao nó, e listaDE, que é uma referência a uma 
    'lista duplamente encadeada.
    """
    def __init__(self, data, listaDE: DoublyLinkedListIterator, nextNode=None):
        self.data = data
        self.listaDE = listaDE
        self.nextNode = nextNode


class SinglyLinkedListIterator:
    """A classe SinglyLinkedListIterator define um iterador para percorrer a lista encadeada. 
    Essa classe possui métodos para adicionar nós na lista, inserir nós em uma posição específica, 
    eliminar nós, definir o nó atual como o primeiro ou último nó da lista, avançar para o próximo 
    nó e mover o iterador para um nó em uma posição específica.
    """
    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode
        if firstNode:
            self.size = 1
        else:
            self.size = 0

    def addNode(self, data: any, listaDE: DoublyLinkedListIterator):
        """O método addNode adiciona um nó ao final da lista encadeada, 
        armazenando o valor passado como parâmetro em data e a referência 
        para a lista duplamente encadeada em listaDE.

        Args:
            data (any): valor a ser armazenado
            listaDE (DoublyLinkedListIterator): lista duplamente encadeada
        """
        newNode = ListNode(data, listaDE)
        newNode.nextNode = None
        if self.size == 0:
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.lastNode:
            self.lastNode.nextNode = newNode
            self.iterator = newNode
            self.lastNode = newNode
        else:
            newNode.nextNode = self.iterator.nextNode
            self.iterator.nextNode = newNode
            self.iterator = newNode
        
        if listaDE != None:
            newNode.listaDE = listaDE
        self.size += 1
        return True

    def insNode(self, data, ListaDE: DoublyLinkedListIterator):
        """O método insNode insere um novo nó antes do nó atual, armazenando o valor passado como parâmetro em data.

        Args:
            data (any): Qualquer valor a ser armazenada.
            ListaDE (DoublyLinkedListIterator): Lista duplamente encadeada
        """
        newNode = ListNode(data, ListaDE)
        newNode.nextNode = None
        if self.size == 0:
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.firstNode:
            newNode.nextNode = self.firstNode
            self.firstNode = newNode
            self.iterator = newNode
        else:
            currentNode = self.firstNode
            while currentNode.nextNode != self.iterator:
                currentNode = currentNode.nextNode
            newNode.nextNode = self.iterator
            currentNode.nextNode = newNode
            self.iterator = newNode
        self.size += 1
        return True

    def elimNode(self):
        """
            O método elimNode remove o nó atual da lista.
        """
        if self.iterator == self.firstNode:
            if self.lastNode == self.firstNode:
                self.lastNode = None
                self.firstNode = None
                self.iterator = None
            else:
                self.firstNode = self.firstNode.nextNode
                self.iterator.nextNode = None
                self.iterator = self.firstNode
        else:
            currentNode = self.firstNode
            while currentNode.nextNode != self.iterator:
                currentNode = currentNode.nextNode
            if self.iterator == self.lastNode:
                self.lastNode = currentNode
                self.iterator.nextNode = None
                self.iterator = None
                currentNode.nextNode = None
            else:
                currentNode.nextNode = self.iterator.nextNode
                currentNode = self.iterator
                self.iterator = self.iterator.nextNode
                currentNode.nextNode = None
        self.size = self.size - 1
        return True

    def first_Node(self):
        """
            O método first_Node define o nó atual como sendo o primeiro nó da lista.
        """
        self.iterator = self.firstNode
        return True

    def last_Node(self):
        """
            O método last_Node define o nó atual como sendo o último nó da lista.
        """
        self.iterator = self.lastNode
        return True

    def nextNode(self):
        """
            O método nextNode avança o iterador para o próximo nó na lista.
        """
        if self.iterator:
            self.iterator = self.iterator.nextNode
        return True

    def posNode(self, position: int):
        """O método posNode move o iterador para um nó em uma 
        posição específica.

        Args:
            position (int): posição para qual o iterador será
            movido.
        """
        if position > 0 and position <= self.size:
            i = 1
            self.iterator = self.firstNode
            while i < position:
                if self.iterator.nextNode is not None:
                    self.iterator = self.iterator.nextNode
                    i = i + 1
            return