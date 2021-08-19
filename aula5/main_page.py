from Stack import Stack


def main():

    input_test = ['Google', 'Gmail', None, 'Globo', 'Twitter', None, None]
    stack = Stack(10)

    for i in input_test:
        if i is None:
            print('Saindo:', stack.pop())
        else:
            print('Entrando: ', i)
            stack.push(i)

        print('Pilha atual: ', stack.data[:len(stack)], end='\n\n')


if __name__ == '__main__':
    main()
