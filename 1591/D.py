problem_num = int(input())
for i in range(problem_num):
    n = input()
    x = input()
    arr = x.split()
    arr = [int(a) for a in arr]
    sorted_arr = arr.copy()
    sorted_arr.sort()
    if len(list(set(arr))) < len(arr):
        print('YES')
        continue
    count = 0
    not_matched = []
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            not_matched.append(arr[i])
            count += 1
    if count % 4 == 2:
        print('NO')
    else:
        print('YES')
