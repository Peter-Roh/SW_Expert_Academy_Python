for i in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    ans = [0] * N
    for j in range(2, N - 2):
        ans[j] = building[j] - max(building[j - 2], building[j - 1], building[j + 1], building[j + 2])
        if ans[j] < 0:
            ans[j] = 0
    print('#{} {}'.format(i, sum(ans)))
