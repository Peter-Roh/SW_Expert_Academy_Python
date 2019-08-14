for i in range(10):
    input()
    arr = []
    sum_arr = []
    t = 0
    for j in range(100):
        arr.append(list(map(int, input().strip().split())))
        sum_arr.append(int(sum(arr[j])))
    for k in range(100):
        for l in range(100):
            t += arr[l][k]
        sum_arr.append(t)
        t = 0
    for k in range(100):
        t += arr[k][k]
        sum_arr.append(t)
        t = 0
    for k in range(100):
        t += arr[99 - t][t]
        sum_arr.append(t)
        t = 0
    print('#{} {}'.format(i + 1, max(sum_arr)))
