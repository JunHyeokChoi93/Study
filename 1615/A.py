problem_num = int(input())
for i in range(problem_num):
    num_buildings = int(input())
    arr = list(map(int,input().split()))
    summation = sum(arr)
    if summation % num_buildings == 0:
        print(0)
    else:
        print(1)
