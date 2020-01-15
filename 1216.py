def is_pali(s, n):
    for i in range(int(n / 2)):
        if(s[i] != s[n - i - 1]):
            return False
    return True

for i in range(10):
    T = int(input())
    ans = 0
    ans_1 = 0
    ans_2 = 0
    arr = [list(input()) for l in range(100)]
    for k in range(100, 0, -1):
        for j in range(100):
            for l in range(101 - k):
                if is_pali(arr[j][l: l + k + 2], k) == True:
                    ans_1 = k
                    break
            if ans_1 != 0:
                break
        if ans_1 != 0:
            break
    arr = [[row[l] for row in arr] for l in range(100)]
    for k in range(100, 0, -1):
        for j in range(100):
            for l in range(101 - k):
                if is_pali(arr[j][l: l + k + 2], k) == True:
                    ans_2 = k
                    break
            if ans_2 != 0:
                break
        if ans_2 != 0:
            break
    if ans_1 > ans_2:
        ans = ans_1
    else:
        ans = ans_2
    print("#{} {}".format(T, ans))
