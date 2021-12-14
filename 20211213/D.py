problem_num = int(input())
for i in range(problem_num):
    n = input()
    x = input()
    arr = x.split()
    arr = [int(a) for a in arr]
    sorted_arr = arr.copy()
    sorted_arr.sort()
    count = 0
    not_matched = []
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            not_matched.append(arr[i])
            count += 1
    if count != 2:
        print('YES')
    else:
        # if arr.count(not_matched[0])>1 or arr.count(not_matched[1])>1:
        if len(list(set(arr)))<len(arr):
            print('YES')
        else:
            print('NO')
