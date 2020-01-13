T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    G = N
    arr = []
    for k in range(N):
        arr.append(0)
    for j in range(M):
        a, b = map(int, input().split())
        if arr[a - 1] == 0 and arr[b - 1] == 0:
            arr[a - 1] = G
            arr[b - 1] = G
            G -= 1
        elif arr[a - 1] != 0 and arr[b - 1] == 0:
            arr[b - 1] = arr[a - 1]
        elif arr[b - 1] != 0 and arr[a - 1] == 0:
            arr[a - 1] = arr[b - 1]
        elif arr[a - 1] != 0 and arr[b - 1] != 0:
            if arr[a - 1] != arr[b - 1]:
                temp = arr[a - 1]
                for k in range(N):
                    if arr[k] == temp:
                        arr[k] = arr[b - 1]
    for l in range(N):
        if arr[l] == 0:
            arr[l] = G
            G -= 1
    print( "#{} {}".format(i, len(set(arr))))
