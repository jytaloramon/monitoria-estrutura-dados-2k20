count_pass = 0


def main():

    data = [
        {'id': '15', 'dist': 52},
        {'id': '56', 'dist': 41},
        {'id': '1', 'dist': 10},
        {'id': '5', 'dist': 2},
        {'id': '2', 'dist': 156},
        {'id': '136', 'dist': 465}
    ]

    print('Antes da Ordenação')
    for d in data:
        print('     - id: {}, dist: {}'.format(d['id'], d['dist']))

    merge_sort(data, 0, len(data))

    print('Depois da Ordenação')
    for d in data:
        print('     - id: {}, dist: {}'.format(d['id'], d['dist']))

    print(f'PASSOS TOTAIS: {count_pass}')

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
        if (data[i]['dist'] <= data[j]['dist']):
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
