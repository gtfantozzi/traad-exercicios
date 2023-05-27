#!/usr/bin/python
# -*- coding: utf-8 -*

class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    @property
    def head(self):
        if self._head is not None:
            return self._head.value
        return None

    @property
    def tail(self):
        if self._tail is not None:
            return self._tail.value
        return None

    def append(self, value):
        """
        Adiciona um novo nó no FINAL da lista.
        Atualiza os ponteiros _head e _tail.
        Incrementa _len p/ controle do tamanho da lista.
        """
        new_node = LinkedListNode(value)
        # se a lista está vazia é o primeiro valor
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        # se não, adiciona novo nó atualizando o
        # next do nó atualmente no _tail p/ apontar pro novo nó
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._len += 1

    def insert(self, value):
        """
        Adiciona um novo nó no INICIO da lista.
        Atualiza os ponteiros _head e _tail.
        Incrementa _len p/ controle do tamanho da lista.
        """
        new_node = LinkedListNode(value)
        # mesma lógica do método 'append'
        if self._head is None: 
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._len += 1

    def removeFirst(self):
        """
        Remove primeiro elemento da lista e retorna o valor.
        Atualiza o contador p/ manter controle da lista.
        """
        if self._head is None:
            return None
        value = self._head.value
        # atualiza _head p/ apontar pro proximo nó
        # assim removemos o primeiro nó
        self._head = self._head.next
        # se era unico valor, mantemos lista vazia
        if self._head is None: 
            self._tail = None
        self._len -= 1
        return value

    def getValueAt(self, index):
        """
        Retorna valor de um nó no indice especifico.
        """
        if index < 0 or index >= self._len:
            raise OutOfBoundsException("Index out of bounds")
        # pega primeiro nó
        current_node = self._head 
        # percorre lista até o indice
        for _ in range(index):
            current_node = current_node.next
        return current_node.value

    def toList(self):
        """
        Retorna uma lista normal de uma lista ligada.
        """
        result = []
        current_node = self._head
        # itera até o fim, adicionando valor do nó na lista
        # atualizando o nó atual p/ apontar pro proximo.
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return result


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    ll = LinkedList()
    assert(ll.head is None)
    assert(ll.tail is None)
    assert(ll.toList() == [])
    ll.append(1)
    assert(ll.head == 1)
    assert(ll.tail == 1)
    assert(len(ll) == 1)
    assert(ll.toList() == [1])
    ll.append(2)
    assert(ll.head == 1)
    assert(ll.tail == 2)
    assert(len(ll) == 2)
    assert(ll.toList() == [1, 2])
    ll.append(3)
    assert(ll.head == 1)
    assert(ll.tail == 3)
    assert(len(ll) == 3)
    assert(ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert(ll.head == 0)
    assert(ll.tail == 3)
    assert(len(ll) == 4)
    assert(ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert(ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == -1)
    assert(ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == 0)
    assert(ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert(v == 1)
    assert(ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert(v == 2)
    assert(ll.toList() == [3])
    v = ll.removeFirst()
    assert(v == 3)
    assert(ll.toList() == [])
    assert(len(ll) == 0)
    print("100%")