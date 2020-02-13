TC = int(input())

for i in range(1, TC + 1):
    N = int(input())
    d_n = []
    while len(d_n) != N:
        temp = list(input().split())
        d_n += temp
    d = str("".join(d_n))
    target = 0
    while True:
        s_target = str(target)
        if s_target not in d:
            break
        target += 1
    print(f"#{i} {target}")
