N, S, M = map(int, input().split())
volume_list = list(map(int, input().split()))

# 1 <= X <= M
table = [[S]]

for i in range(1, N + 1):
    count = 0
    table.append(set())

    for j in table[i - 1]:

        if j + volume_list[i - 1] <= M:
            count += 1
            table[i].add(j + volume_list[i - 1])

        if j - volume_list[i - 1] >= 0:
            count += 1
            table[i].add(j - volume_list[i - 1])

    if count == 0:
        print(-1)
        exit()
    
print(max(table[N]))
