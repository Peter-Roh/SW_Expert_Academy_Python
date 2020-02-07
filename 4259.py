def calc(a):
    ex = a % 10
    base = int((a - ex) / 10)
    return base**ex

tc = int(input())

for i in range(tc):
    n = int(input())
    num = [0] * n
    ans = [0] * n
    num = list(map(int, input().split(" ")))
    for j in range(n):
        ans[j] = calc(num[j])
    print("#{} {}".format(i + 1, sum(ans)))
