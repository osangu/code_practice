n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

mem = costs[0].copy()
for i in range(1, n):
    last_mem = mem.copy()
    mem[0] = costs[i][0] + min(last_mem[1], last_mem[2])
    mem[1] = costs[i][1] + min(last_mem[0], last_mem[2])
    mem[2] = costs[i][2] + min(last_mem[0], last_mem[1])

print(min(mem))
