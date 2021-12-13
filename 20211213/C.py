problem_num = int(input())
for i in range(problem_num):
    nk = input()
    nk = nk.split()
    n = int(nk[0]);k = int(nk[1])
    x = input()
    arr = x.split()
    pos = [int(a) for a in arr if int(a) >= 0]
    neg = [abs(int(a)) for a in arr if int(a) < 0]
    pos.sort(reverse=True)
    pos = pos[::k]
    neg.sort(reverse=True)
    neg = neg[::k]
    max_value = max(pos + neg)
    print(2*sum(pos+neg)-max_value)


