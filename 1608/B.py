problem_num = int(input())
for i in range(problem_num):
    arr = list(map(int,input().split()))
    if abs(arr[1]-arr[2])>2 or arr[1] + arr[2] > arr[0] - 2:
        print(-1)
        continue
    init = 10 ** 6
    if arr[1]>arr[2]:

    elif arr[1]<arr[2]

