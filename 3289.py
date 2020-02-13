def find(arr, n):
    if n == arr[n]:
        return n
    else:
        p = find(arr, arr[n])
        arr[n] = p
        return p

def union(arr, a, b):
    x = find(arr, a)
    y = find(arr, b)
    if x != y:
        arr[y] = x

def check(arr, a, b):
    x = find(arr, a)
    y = find(arr, b)
    if x == y:
        return '1'
    else:
        return '0'

TC = int(input())

for i in range(1, TC + 1):
    n, m = map(int, input().split())
    arr = [0] * (n + 1)
    for j in range(n + 1):
        arr[j] = j
    ans = ""
    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            union(arr, a, b)
        elif c == 1:
            ans += check(arr, a, b)
    print(f"#{i} {ans}")
