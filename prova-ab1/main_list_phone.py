count_pass = 0


def main():

    data_input = [
        {'nome': 'ramon', 'telefone': '1111'},
        {'nome': 'zeca', 'telefone': '2222'},
        {'nome': 'ana', 'telefone': '333'},
        {'nome': 'beatriz', 'telefone': '4444'},
        {'nome': 'maria', 'telefone': '5555'}
    ]

    list_phone = []

    for ipt in data_input:
        print(' * INSERINDO', ipt,)
        insert_phone(ipt, list_phone)

        for d in list_phone:
            print('     - {}, {}'.format(d['nome'], d['telefone']))

    print(f'PASSOS TOTAIS: {count_pass}')

    # Complexidade pior caso O(n²)


def insert_phone(data, list_phone):

    global count_pass
    list_phone.append(None)
    i = len(list_phone) - 2

    while i >= 0 and list_phone[i]['nome'] > data['nome']:
        list_phone[i + 1] = list_phone[i]
        i -= 1
        count_pass += 1

    list_phone[i + 1] = data
    count_pass += 1


main()
