per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = [int(i * money * 0.01) for i in per_cent.values()]
print(deposit)
print(f'Максимальная сумма, которую вы можете заработать — {max(deposit)}')


if __name__ == '__main__':
    print_hi('PyCharm')

