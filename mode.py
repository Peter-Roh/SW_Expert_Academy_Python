for i in range(int(input())):
    n = input()
    score = list(map(int, input().split()))
    cnt = [score.count(j) for j in range(100, 0, -1)]
    print('#' + n + ' ' + str(100 - cnt.index(max(reversed(cnt)))))
