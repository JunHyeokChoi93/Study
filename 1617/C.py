problem_num = int(input())
for i in range(problem_num):
    n = int(input())
    arr = list(map(int, input().split()))
    target = set(range(1, n + 1))
    target_arr = set()
    target_dup = []
    for i in range(n):
        if arr[i] in target and arr[i] not in target_arr:
            target_arr.add(arr[i])
        else:
            target_dup.append(arr[i])
    dum = list(target - target_arr)
    pr = 0
    dum.sort()
    target_dup.sort()
    for i in range(len(target_dup)):
        if (target_dup[i] - 1) // 2 < dum[i]:
            pr = -1
            break
    if pr:
        print(-1)
    else:
        print(len(target_dup))


