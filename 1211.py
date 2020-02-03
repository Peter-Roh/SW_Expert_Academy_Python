def go(data, i, j, cnt):
    i += 1
    cnt += 1
    while i != 99:
        if j == 0:
            while j < 99 and data[i][j + 1] == 1:
                j += 1
                cnt += 1
        elif j == 99:
            while j > 0 and data[i][j - 1] == 1:
                j -= 1
                cnt += 1
        elif j > 0 and j < 99:
            if data[i][j - 1] == 1:
                while j > 0 and data[i][j - 1] == 1:
                    j -= 1
                    cnt += 1
            elif data[i][j + 1] == 1:
                while j < 99 and data[i][j + 1] == 1:
                    j += 1
                    cnt += 1
        i += 1
        cnt += 1
    return cnt

for _ in range(10):
    TC = int(input())
    data = [list(map(int, input().strip().split(" "))) for i in range(100)]
    start = []
    for i in range(100):
        if data[0][i] == 1:
            start.append(i)
    l = len(start)
    ans = [0] * l
    for j in range(l):
        x_index = 0
        y_index = start[j]
        cnt = 0
        temp = go(data, x_index, y_index, cnt)
        ans[j] = temp
    answer = ans.index(min(ans))
    print("#{} {}".format(TC, start[answer]))
