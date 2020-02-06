tc = int(input())

for t in range(tc):
    W = input().strip()
    l = len(W)
    arr = [0] * 26
    ans = 0
    for i in range(l):
        arr[ord(W[i]) - 97] += 1
    for i in arr:
        ans += int(i * (i + 1) / 2)
    print("#{} {}".format(t + 1, ans))
