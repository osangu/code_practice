N = int(input())
table = []
for i in range(N):
    if i == 0:
        num_list = [int(input())]
    else:
        num_list = list(map(int, input().split()))

    table.append(num_list)


for i, j in enumerate(table):
    for l, k in enumerate(j):
        if i == N - 1:
            break

        elif i == 0:
            table[i + 1][l] += k
            table[i + 1][l + 1] += k
        else:
            if l == 0:
                table[i + 1][l] += k
                table[i + 1][l + 1] = [table[i + 1][l + 1], table[i + 1][l + 1] + k]
            else:
                table[i + 1][l] = max([table[i + 1][l][1], table[i + 1][l][0] + k])

                if l == len(j) - 1:
                    table[i + 1][l + 1] += k

                else:
                    table[i + 1][l + 1] = [table[i + 1][l + 1], table[i + 1][l + 1] + k]

print(max(table[-1]))
