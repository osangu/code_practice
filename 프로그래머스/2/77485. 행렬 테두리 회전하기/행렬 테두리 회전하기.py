from collections import deque

def solution(rows, columns, queries):
    answer = []
    table = []
    view = []
    for i in range(1, rows * columns + 1):
        view.append(i)
        if i % columns == 0:
            table.append(view)
            view = []

    for q in queries:
        x = (q[0] - 1, q[1] - 1)
        y = (q[2] - 1, q[3] - 1)

        top_row = deque(table[x[0]][x[1]:y[1] + 1])
        bottom_row = deque(table[y[0]][x[1]:y[1] + 1])

        left_column = deque([table[i][x[1]] for i in range(x[0], y[0] + 1)])
        right_column = deque([table[i][y[1]] for i in range(x[0], y[0] + 1)])

        answer.append(min(top_row + bottom_row + left_column + right_column))

        right_column.appendleft(top_row[-2])
        bottom_row.popleft()
        bottom_row.append(right_column[-2])
        top_row.pop()
        left_column.popleft()
        top_row.appendleft(left_column[0])
        right_column.pop()

        table[x[0]][x[1]:y[1] + 1] = top_row
        table[y[0]][x[1]:y[1] + 1] = bottom_row

        for i, v in enumerate(range(x[0], y[0] + 1)):
            if i - 1 < 0: continue

            table[v - 1][x[1]] = left_column[i - 1]

        for i, v in enumerate(range(x[0], y[0] + 1)):

            if i - 1 < 0: continue
            table[v - 1][y[1]] = right_column[i - 1]

    return answer
