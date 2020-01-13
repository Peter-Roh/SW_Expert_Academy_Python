T = int(input())

for i in range(T):
    arr = []
    N = int(input())
    while N > 0:
        a, b = map(float, input().split())
        arr.append(a * b)
        N -= 1
    print("#{} {:.6f}".format(i + 1, sum(arr)))
