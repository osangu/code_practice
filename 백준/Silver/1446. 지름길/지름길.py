N, M = map(int, input().split())

short_way = {}
table = [[(0, 0)]]

for i in range(N):
    a, b, c = map(int, input().split())

    if a > M:
        continue
        
    if short_way.get(a):
        if short_way[a].get(b):
            short_way[a][b] = min(c, short_way[a][b])
        else:
            short_way[a][b] = c

    else:
        short_way[a] = {b: c}

for i, start in enumerate(sorted(short_way.keys())):
    table.append([])

    for end in short_way[start]:
        length = short_way[start][end]

        for loc in table[i]:
            location, distance = loc

            if location > start:
                table[i + 1].append(loc)
                continue

            # move
            table[i + 1].append((end, (start - location) + distance + length))

            # not move
            table[i + 1].append((start, (start - location) + distance))

print(min(M - i[0] + i[1] for i in table[-1] if i[0] <= M))
