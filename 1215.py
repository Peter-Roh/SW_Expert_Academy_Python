def is_pali(s, n):
    t = 0
    for i in range(int(n / 2)):
        if s[i] != s[n - i - 1]:
            t = 1;
            break
    return t

for i in range(10):
    arr_alph = []
    cnt = 0
    n = int(input())
    for j in range(8):
        arr_alph.append(list(input()))
    for j in range(8):
        for k in range(0, 9 - n):
            if is_pali(arr_alph[j][k : k + n + 1], n) == 0:
                cnt += 1
    arr_alph = [[row[l] for row in arr_alph] for l in range(8)]
    for j in range(8):
        for k in range(0, 9 - n):
            if is_pali(arr_alph[j][k : k + n + 1], n) == 0:
                cnt += 1
    print('#{} {}'.format(i + 1, cnt))
