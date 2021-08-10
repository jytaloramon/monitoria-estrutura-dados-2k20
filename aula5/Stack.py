class Stack:

    def __init__(self, size):
        if (size < 1):
            raise Exception('Size deve ser maior que 0')

        self.length = -1
        self.size = size
        self.data = [None for i in range(size)]

    def __len__(self):
        return self.length + 1

    def is_empty(self):
        return self.__len__() == 0

    def is_full(self):
        return self.__len__() == self.size

    def push(self, elemn):
        if self.is_full():
            raise Exception('Pilha cheia')

        self.length += 1
        self.data[self.length] = elemn

    def pop(self):
        if self.is_empty():
            raise Exception('Pilha vazia')

        elmnt = self.data[self.length]
        self.data[self.length] = None
        self.length -= 1

        return elmnt

    def peek(self):
        if self.is_empty():
            raise Exception('Pilha vazia')

        return self.data[self.length]

    def __str__(self):
        if self.is_empty():
            return 'Pilha vazia'

        return ' ,'.join(self.data[:self.__len__()])
