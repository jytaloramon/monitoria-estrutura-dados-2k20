import os


def main():

    # Informações do arquivo
    dir_name_work, file_name_work = './aula2', 'texto.txt'

    # Leitura dos dados
    os.chdir(dir_name_work)
    text = open(file_name_work).read().replace('\n', '')

    # Quebrando o texto em palavras: "Vou viajar" -> ['Vou', 'viajar']
    words = text.split(' ')
    # Ordenação por ordem alfabética das palavras
    bubble_sort(words)
    # Contando as palavras do texto
    words_info = words_count(words)

    print("Infomações das palavras:", end='\n  - ')
    for i, item in enumerate(words_info):
        print(f'{item}', end='\n  - ' if ((i + 1) % 5) == 0 else ', ')

    print("\n\nBusca Binária")
    words_find = ['algoritmo', 'arquivo', 'casa',
                  'texto', 'exiba', 'carro', 'implementar']

    for item in words_find:
        print(f'  - {item}: ', end='')

        rs = b_search(item, words_info)
        if (not (rs is None)):
            print(rs)
        else:
            print('Não encontrado')


def bubble_sort(arr):
    # Complexida O(n²)

    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def words_count(words):
    # Complexidade O(n)

    words_sv = []
    i, j = 1, 0

    while i < len(words):
        if (words[i] != words[j]):
            words_sv.append((words[j], i - j))
            j = i
        i += 1

    words_sv.append((words[j], i - j))

    return words_sv


def b_search(word_f, words):
    # Complexidade O(log(n)): log(n) na base 2
    # Implementação iterativa da busca binária.

    start, end, middle = 0, len(words) - 1, 0

    while start <= end:

        middle = (start + end) // 2

        if (words[middle][0] == word_f):
            return words[middle]

        if (words[middle][0] > word_f):
            end = middle - 1
        else:
            start = middle + 1

    return None


if __name__ == '__main__':
    main()
