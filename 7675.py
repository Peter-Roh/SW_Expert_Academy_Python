T = int(input())

def isName(name):
    l = len(name)
    if name.isalpha() == False:
        return False

    if l == 1:
        if name.isupper() == True:
            return True
        else:
            return False
    else:
        if name[0].isupper() == True and name[1:].islower() == True:
            return True
        else:
            return False

for i in range(1, T + 1):
    N = int(input())
    ans = [0] * N
    cnt = 0
    sen = input().replace('?', '.').replace('!', '.').split('.')
    del sen[-1]
    for j in range(N):
        temp = sen[j].strip().split(" ")
        for item in temp:
            if isName(item) == True:
                cnt += 1
        ans[j] = cnt
        cnt = 0
    print('#{}'.format(i), end=' ')
    for j in range(N):
        print('{}'.format(ans[j]), end=' ')
    print()
