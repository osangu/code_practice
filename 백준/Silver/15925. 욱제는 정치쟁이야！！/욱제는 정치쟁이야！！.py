'''
https://degurii.tistory.com/37

다시 풀기!!
'''
N, M = map(int, input().split())

table = [
    list(map(int, input().split()))
    for i in range(N)
]


def foo():
    for i in range(N):
        cnt = 0
        for j in range(N):
            if table[i][j] == M:
                cnt += 1

        if cnt > N // 2:
            for j in range(N):
                table[i][j] = M

    for j in range(N):
        cnt = 0
        for i in range(N):
            if table[i][j] == M:
                cnt += 1

        if cnt > N // 2:
            for i in range(N):
                table[i][j] = M


foo()
foo()

for i in range(N):
    for j in range(N):
        if table[i][j] != M:
            print(0)
            exit()

print(1)
