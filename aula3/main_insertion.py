count_pass = 0  # Contador de passos executados


def main():

    global count_pass

    print('******** INSERTION SORT ********')

    print('\n')

    arr = [0, 2, 8, 7, 8, 5, 9, 3, 2, 1]
    print(f'Arr. origem ({len(arr)}): {arr}')

    insertion_sort(arr, 0, len(arr))
    print(f'Arr. sorted: {arr}')
    print(f'Count_pass: {count_pass}')

    print('\n')

    # Teste com array com 1000 elementos em ordem decrescente
    count_pass = 0
    arr = list(range(1000, -1, -1))
    print(f'Arr. origem ({len(arr)}): {arr}')

    insertion_sort(arr, 0, len(arr))
    print(f'Arr. sorted: {arr}')
    print(f'Count_pass: {count_pass}')

    # Selection Sort: complexidade O(n²)


def insertion_sort(data, start_i, end_i):
    # Complexida O(n²)

    posi_min_actual = 0
    global count_pass

    for i in range(start_i + 1, end_i):
        j, base = i - 1, data[i]

        while j >= 0 and data[j] > base:
            data[j + 1] = data[j]
            j -= 1
            count_pass += 1

        data[j + 1] = base
        count_pass += 1


main()
