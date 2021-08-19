from Stack import Stack


def main():

    input_test = [11, 1, 2, 4, 3, 10, 9, 8,  0, 5, -1, -5]
    len_numbers = len(input_test)

    stack, stack_aux = Stack(len_numbers), Stack(len_numbers)

    for i in input_test:
        stack_aux.push(i)

    stack.push(stack_aux.pop())
    while not(stack_aux.is_empty()):
        actual = stack_aux.pop()
        if stack.peek() <= actual:
            stack.push(actual)
        else:
            while not(stack.is_empty()) and actual < stack.peek():
                stack_aux.push(stack.pop())
            stack.push(actual)

    print(stack.data)


if __name__ == '__main__':
    main()
