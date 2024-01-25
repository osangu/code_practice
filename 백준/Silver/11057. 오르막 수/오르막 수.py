table = {}
table[1] = {'sum': 9, 'list': [1] * 9}

N = int(input())

for i in range(2, N + 1):
    table[i] = {'sum': 0, 'list': []}

    for j, v in enumerate(table[i - 1]['list']):
        if j == 0:
            table[i]['list'].append(table[i - 1]['sum'] % 10007)
        else:
            ans = table[i]['list'][-1] - table[i - 1]['list'][j - 1] % 10007
            table[i]['list'].append(ans)

        table[i]['sum'] += table[i]['list'][-1]

answer = 1
for i in table:
    answer += table[i]['sum']

print(answer % 10007)