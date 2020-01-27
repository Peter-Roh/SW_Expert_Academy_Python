def go(data, i, j):
    i += 1
    while i != 99:
        if j == 0:
            while j < 99 and data[i][j + 1] == 1:
                j += 1
        elif j == 99:
            while j > 0 and data[i][j - 1] == 1:
                j -= 1
        elif j > 0 and j < 99:
            if data[i][j - 1] == 1:
                while j > 0 and data[i][j - 1] == 1:
                    j -= 1
            elif data[i][j + 1] == 1:
                while j < 99 and data[i][j + 1] == 1:
                    j += 1
        i += 1
    if data[99][j] == 2:
        return j
    else:
        return -1

for i in range(10):
    tc = int(input())
    data = [list(map(int, input().strip().split(" "))) for j in range(100)]
    start = []
    for j in range(100):
        if data[0][j] == 1:
            start.append(j)
    for s in start:
        x_index = 0
        y_index = s
        ans = go(data, x_index, y_index)
        if ans >= 0:
            print("#{} {}".format(tc, s))
            break
