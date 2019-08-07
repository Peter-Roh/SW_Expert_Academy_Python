def func_check():
    for i in range(len(num)):
        if num[i] != max_num[i]:
            check[i] = 1
        else:
            check[i] = 0

for T in range(int(input())):
    num, cnt = map(int, input().split())
    num = str(num)
    max_num = sorted(num, reverse=True)
    check = [0] * len(num)
    func_check()
    i = 0
    while cnt > 0:
        cnt -= 1
        if ''.join(max_num) == num:
            for k in range(len(num) - 1):
                if num[k] == num[k + 1]:
                    break
            else:
                num = list(num)
                num[-1:], num[-2:-1] = num[-2:-1], num[-1:]
                num = ''.join(num)
                del check[-2:]
                check.append(1)
                check.append(1)
        else:
            num = list(num)
            while check[i] == 0:
                i += 1
            check[i] = 0
            for j in range(len(num)):
                if num[j] == max_num[i]:
                    if check[j] == 1:
                        num[i], num[j] = num[j], num[i]
                        check[j] = 0
                        break
            func_check()
            num = ''.join(num)
    print('#{} {}'.format(T + 1, num))
