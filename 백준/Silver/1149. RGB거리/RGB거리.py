N = int(input())

table = [
    list(map(lambda x: [int(x)], input().split()))
    for i in range(N)
]


def get_answer(r, g, b):
    return min(r[0], g[0], b[0])


for i in range(1, N):
    for j in range(3):
        if j == 0:
            add = min(
                table[i - 1][1][0],
                table[i - 1][2][0]
            )
            table[i][0][0] += add

        elif j == 1:
            add = min(
                table[i - 1][0][0],
                table[i - 1][2][0]
            )
            table[i][1][0] += add

        elif j == 2:
            add = min(
                table[i - 1][0][0],
                table[i - 1][1][0]
            )
            table[i][2][0] += add
            
print(get_answer(*table[N - 1]))
