count_pass = 0  # Contador de passos executados


def main():

    global count_pass

    print('******** QUICK SORT ********')

    print('\n')

    arr = [0, 2, 8, 7, 8, 5, 9, 3, 2, 1]
    print(f'Arr. origem: {arr}')

    quick_sort(arr, 0, len(arr))
    print(f'Arr. sorted: {arr}')
    print(f'Count_pass: {count_pass}')

    print('\n')

    # Teste com array com 1000 elementos em ordem decrescente
    # Provavelemente não irá roda (com tamanho de 1000)
    #   pois o interpretador Python irá bloquear devido
    #   ao grande número de chamadas recursivas.
    # Vc pode configurar para permitir mais ou diminuir o tamanho.
    count_pass = 0
    arr = list(range(1000, -1, -1))
    print(f'Arr. origem ({len(arr)}): {arr}')

    quick_sort(arr, 0, len(arr))
    print(f'Arr. sorted: {arr}')
    print(f'Count_pass: {count_pass}')

    # Quick Sort: complexidade => Pior caso: O(n²); Médio: O(n * log(n))


def quick_partition(data, s_i, e_i):
    # Complexida => O(n)

    v_pivot = data[s_i]
    i, j = s_i + 1, e_i - 1
    global count_pass

    while i <= j:
        while i < e_i and data[i] <= v_pivot:
            i += 1
            count_pass += 1

        while j >= 0 and data[j] > v_pivot:
            j -= 1
            count_pass += 1

        if (i <= j):
            data[i], data[j] = data[j], data[i]

        count_pass += 2

    data[j], data[s_i] = data[s_i], data[j]

    return j


def quick_sort(data, s_i, e_i):
    # Complexida => Pior caso: O(n); Melhor caso O(log(n))

    global count_pass
    count_pass += 1

    if (s_i >= e_i - 1):
        return

    idx_pivot = quick_partition(data, s_i, e_i)
    quick_sort(data, s_i, idx_pivot)
    quick_sort(data, idx_pivot + 1, e_i)


main()
