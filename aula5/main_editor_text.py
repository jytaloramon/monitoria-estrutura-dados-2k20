from Stack import Stack


def main():

    status = True
    text = ''
    stack = Stack(100)
    operation = ('rm', 'add')

    while status:
        print(text, end='\n\n')
        status = bool(int(input('Continuar (0 = N; 1 = S)? ')))

        if not(status):
            continue

        op = int(
            input('[0] Remover Texto (caracteres)\n[1] Adicionar texto\n[2] Desfazer (quant.)\n => '))
        if op == 1:
            text_add = input('Texto: ')
            stack.push((operation[op], len(text_add)))
            text += text_add
            continue

        len_t = int(input('Quantidade: '))
        if op == 0:
            if len(text) - len_t > 0:
                stack.push((operation[op], text[len(text) - len_t:]))
                text = text[:len(text) - len_t]
        else:
            if len_t <= len(stack):
                for i in range(len_t):
                    inf = stack.pop()

                    if inf[0] == operation[0]:
                        text += inf[1]
                    else:
                        text = text[:len(text) - inf[1]]

    print(text)


if __name__ == '__main__':
    main()
