count_pass = 0  # Contador de passos executados


def main():

    global count_pass

    print('******** Merge SORT ********')

    print('\n')

    arr = [0, 2, 8, 7, 8, 5, 9, 3, 2, 1]
    print(f'Arr. origem: {arr}')

    merge_sort(arr, 0, len(arr))
    print(f'Arr. sorted: {arr}')
    print(f'Count_pass: {count_pass}')

    print('\n')

    # Teste com array com 1000 elementos em ordem decrescente
    count_pass = 0
    arr = list(range(1000, -1, -1))
    print(f'Arr. origem ({len(arr)}): {arr}')

    merge_sort(arr, 0, len(arr))
    print(f'Arr. sorted: {arr}')
    print(f'Count_pass: {count_pass}')

    # Merge Sort: complexidade O(n * log(n))


def merge_sort(data, start_i, end_i):
    # Complexidade: O(log(n))

    global count_pass
    count_pass += 1

    if (start_i == end_i - 1):
        return

    middle = (start_i + end_i) // 2

    merge_sort(data, start_i, middle)
    merge_sort(data, middle, end_i)
    merge_sort_curr(data, start_i, middle, end_i)


def merge_sort_curr(data, start_i, middle, end_i):
    # Complexida O(n): Linear

    arr_aux = [0] * (end_i - start_i)
    i, j, t = start_i, middle, 0
    global count_pass

    while i < middle and j < end_i:
        if (data[i] <= data[j]):
            arr_aux[t] = data[i]
            i += 1
        else:
            arr_aux[t] = data[j]
            j += 1
        t += 1
        count_pass += 1

    while i < middle:
        arr_aux[t] = data[i]
        i += 1
        t += 1
        count_pass += 1

    while j < end_i:
        arr_aux[t] = data[j]
        j += 1
        t += 1
        count_pass += 1

    for s in range(t):
        data[start_i + s] = arr_aux[s]
        count_pass += 1


main()
