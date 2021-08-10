from Stack import Stack


def main():

    harbor = Harbor(4, 5)

    harbor.push_container('a')
    print(harbor)
    harbor.push_container('b')
    print(harbor)
    harbor.push_container('c')
    print(harbor)
    harbor.push_container('d')
    print(harbor)
    harbor.push_container('e')
    print(harbor)
    harbor.push_container('f')
    print(harbor)
    harbor.push_container('g')
    print(harbor)
    harbor.push_container('h')
    print(harbor)
    harbor.pop_container(0)
    print(harbor)
    harbor.push_container('i')
    print(harbor)
    harbor.push_container('j')
    print(harbor)
    harbor.pop_container(0, 2)
    print(harbor)
    harbor.pop_container(1, 1)
    print(harbor)


class Harbor():

    def __init__(self, size, size_stack):
        self.size = size
        self.size_stack = size_stack
        self.stacks = [Stack(size_stack) for i in range(size + 1)]

    def __stack_min__(self):
        idx_min_len, min_len = 0, self.size_stack + 1

        for i in range(self.size):
            if len(self.stacks[i]) < min_len:
                min_len = len(self.stacks[i])
                idx_min_len = i

        return self.stacks[idx_min_len]

    def push_container(self, elmnt):
        stack = self.__stack_min__()

        try:
            stack.push(elmnt)
        except Exception:
            print('Não há pilha disponível')

    def pop_container(self, idx_stack, posi_elmnt=0):
        stack = self.stacks[idx_stack]

        if posi_elmnt > len(stack):
            raise Exception('Posição inválida')

        for i in range(posi_elmnt):
            self.stacks[self.size].push(stack.pop())

        elmnt = stack.pop()

        while not(self.stacks[self.size].is_empty()):
            stack.push(self.stacks[self.size].pop())

        return elmnt

    def __str__(self):
        return '\n'.join(map(lambda x: x.__str__(), self.stacks[:self.size])) + '\n-------\n'


if __name__ == '__main__':
    main()
