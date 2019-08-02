for i in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    for j in range(N):
        m = max(box)
        n = min(box)
        box[box.index(m)] -= 1
        box[box.index(n)] += 1
    print('#{} {}'.format(i, max(box) - min(box)))
