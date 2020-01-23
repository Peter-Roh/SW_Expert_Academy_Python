T = int(input())

for i in range(T):
    str = input()
    N = len(str)
    l = N * 4 + 1
    flag = 1
    L1 = []
    L1.append(".")
    L1.append(".")
    for j in range(N - 1):
        L1.append("#")
        L1.append(".")
        L1.append(".")
        L1.append(".")
    L1.append("#")
    L1.append(".")
    L1.append(".")
    L2 = []
    for j in range(l):
        if flag == 1:
            L2.append(".")
            flag = 0
        elif flag == 0:
            L2.append("#")
            flag = 1
    L3 = []
    for j in range(N):
        L3.append("#")
        L3.append(".")
        L3.append(str[j])
        L3.append(".")
    L3.append("#")
    L1 = ''.join(L1)
    L2 = ''.join(L2)
    L3 = ''.join(L3)
    print(L1)
    print(L2)
    print(L3)
    print(L2)
    print(L1)
