from Stack import Stack


def main():

    expressions_test = ['(A*(B+(C*(D+(E*(F+G))))))', '5-[4+(0-3]',
                        '{5-[(4+(0-3))]}', '3-[15+2*(4-3)*[2+(5-1)]]/4', '{5-[(4+(0-3))]})']
    tokens = [('(', ')'), ('[', ']'), ('{', '}')]

    for exp in expressions_test:
        print(exp, ': Válida' if expresion_is_valid(
            exp, tokens) else ': Inválida')


def expresion_is_valid(exp, tks):

    stack = Stack(len(exp))
    tokens = Tokens(tks)

    for el in exp:

        rs = tokens.find(el)
        if not(rs is None):
            if el == rs[0]:
                stack.push(el)
            else:
                if len(stack) == 0 or not(stack.peek() == rs[0]):
                    return False
                stack.pop()

    return stack.is_empty()


class Tokens:

    def __init__(self, tokens):
        self.tokens = tokens

    def find(self, elemnt):

        for e in self.tokens:
            if e[0] == elemnt or e[1] == elemnt:
                return e

        return None


if __name__ == '__main__':
    main()
