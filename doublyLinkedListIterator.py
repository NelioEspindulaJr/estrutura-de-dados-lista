class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedListIterator:
    """
A classe DoublyLinkedListIterator é uma classe que implementa um iterador 
para percorrer uma lista duplamente encadeada. Ela possui métodos para adicionar, 
inserir e eliminar nós, além de métodos para mover o iterador para o início, fim, 
próximo ou anterior nó da lista. Também é possível posicionar o iterador em um nó 
específico pelo índice.

    """

    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode
        self.size = 0 if firstNode is None else 1
        

    def addNode(self, data: any):
        """Esse método adiciona um novo nó depois do nó atual que está sendo apontado pelo iterador. 
        Ele cria um novo nó com os dados fornecidos, ajusta as referências do novo nó e dos nós ao 
        seu redor e incrementa o tamanho da lista.

        Args:
            data (any): valor a ser armazenado
        """
        newNode = Node(data)
        if self.iterator is None:
            self.iterator = newNode
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            newNode.prev = self.iterator
            newNode.next = self.iterator.next
            if self.iterator.next is not None:
                self.iterator.next.prev = newNode
            else:
                self.lastNode = newNode
            self.iterator.next = newNode
        self.size += 1

    def insNode(self, data: any):
        """Esse método insere um novo nó antes do nó atual que está sendo apontado pelo iterador.
        Ele funciona de maneira semelhante ao método addNode(), mas ajusta as referências dos nós 
        de maneira diferente.

        Args:
            data (any): valor a ser armazenado
        """
        newNode = Node(data)
        if self.iterator is None:
            self.iterator = newNode
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            newNode.prev = self.iterator.prev
            newNode.next = self.iterator
            if self.iterator.prev is not None:
                self.iterator.prev.next = newNode
            else:
                self.firstNode = newNode
            self.iterator.prev = newNode
        self.size += 1

    def elimNode(self):
        """Esse método remove o nó atual que está sendo apontado pelo iterador. 
        Ele ajusta as referências do nó anterior e posterior para que eles apontem 
        um para o outro e depois move o iterador para o próximo nó na lista. 
        O tamanho da lista é decrementado.
        """
        if self.iterator is not None:
            if self.iterator.prev is not None:
                self.iterator.prev.next = self.iterator.next
            else:
                self.firstNode = self.iterator.next
            if self.iterator.next is not None:
                self.iterator.next.prev = self.iterator.prev
            else:
                self.lastNode = self.iterator.prev
            self.iterator = self.iterator.next
            self.size -= 1

    def first_Node(self):
        """Esse método move o iterador para o primeiro nó da lista.
        """
        self.iterator = self.firstNode

    def last_Node(self):
        """Esse método move o iterador para o último nó da lista.
        """
        self.iterator = self.lastNode

    def nextNode(self):
        """Esse método move o iterador para o próximo nó na lista, se houver, 
        e retorna False. Se o iterador estiver apontando para o último nó da 
        lista, ele retornará True.

        Returns:
            boolean
        """
        if self.iterator is not None:
            self.iterator = self.iterator.next
            if self.iterator is None:
                return True
        return False

    def anttNode(self):
        """Esse método move o iterador para o nó anterior na lista, se houver, 
        e retorna False. Se o iterador estiver apontando para o primeiro nó da 
        lista, ele retornará True.

        Returns:
            boolean
        """
        if self.iterator is not None:
            self.iterator = self.iterator.prev
            if self.iterator is None:
                return True
        return False

    def posNode(self, position: int):
        """Esse método move o iterador para o nó na posição especificada na lista. 
        Ele faz isso iterando pelos nós na lista até que a posição seja encontrada 
        e ajustando o iterador. Se a posição especificada estiver além dos limites 
        da lista, o iterador será movido para o primeiro ou o último nó, conforme 
        apropriado, e o método retornará True.

        Args:
            position (int): posição a qual o iterador será movido.

        Returns:
            boolean
        """
        if position <= 1:
            self.first_Node()
        elif position >= self.size:
            self.last_Node()
        else:
            currentPos = 1
            currentNode = self.firstNode
            while currentPos < position and currentNode is not None:
                currentNode = currentNode.next
                currentPos += 1
            self.iterator = currentNode
        if self.iterator is None:
            return True
        return False

    def undefinedIterator(self):
        """Esse método verifica se o iterador está definido, ou seja, se ele está 
        apontando para um nó na lista. Ele retorna True se o iterador não estiver 
        definido e False caso contrário.

        Returns:
            boolean
        """
        return self.iterator is None


