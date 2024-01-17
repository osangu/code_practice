N = int(input())

table = [
    list(map(lambda x: [int(x)], input().split()))
    for i in range(N)
]


for i in range(1, N):
    for j in range(3):
        if j == 0:
            add = min(
                table[i - 1][1][0],
                table[i - 1][2][0]
            )

        elif j == 1:
            add = min(
                table[i - 1][0][0],
                table[i - 1][2][0]
            )

        elif j == 2:
            add = min(
                table[i - 1][0][0],
                table[i - 1][1][0]
            )

        table[i][j][0] += add

print(min(*table[N - 1])[0])
