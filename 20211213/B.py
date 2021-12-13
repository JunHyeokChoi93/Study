problem_num = int(input())
for i in range(problem_num):
    nums = int(input())
    x = input()
    arr = x.split()
    arr = [int(a) for a in arr]
    arr = arr[::-1]
    max_val = max(arr)
    init = arr[0]
    count = 0
    for j in range(arr.index(max_val)+1):
        if arr[j] > init:
            init = arr[j]
            count += 1
    print(count)


