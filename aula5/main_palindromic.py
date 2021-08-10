from Stack import Stack


def main():

    word_test = ['ovo', 'ananaa', 'casa', 'taxi' 'radar', 'reviver', 'ana']

    for word in word_test:

        stack = Stack(len(word) // 2)
        i, j, end_w = 0, len(word) - 1,  len(word) // 2

        while i < end_w and stack.is_empty():
            stack.push(word[i])

            if stack.peek() == word[j]:
                stack.pop()

            i += 1
            j -= 1

        if stack.is_empty():
            print(f'{word}: é palíndromo')
        else:
            print(f'{word}: não é palíndromo', '->',
                  f'Status final da pilha {stack.data[:len(stack)]}')


if __name__ == '__main__':
    main()
