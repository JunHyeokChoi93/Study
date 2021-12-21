problem_num = int(input())
for i in range(problem_num):
    n = int(input())
    arr = list(map(int,input().split()))
    target = set(range(1,n+1))
    target_arr = set()
    target_dup = []
    for a in arr:
        if a in target and a not in target_arr:
            target_arr.add(a)
        else:
            target_dup.append(a)
    target_dup.sort()
    dum = list(target - target_arr)
    flag = False
    for i in range(len(dum)):
        if dum[i] > (target_dup[i] + 1) // 2 - 1:
            prn = -1
            flag = True
            break
    if flag:
        print(prn)
    else:
        print(len(target_dup))



