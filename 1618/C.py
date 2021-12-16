import math
problem_num = int(input())
for i in range(problem_num):
    num = int(input())
    arr = input().split()
    arr = [int(a) for a in arr]
    odd_arr = arr[::2]
    even_arr = arr[1::2]
    x = odd_arr[0]
    for j in range(len(odd_arr)-1):
        x = math.gcd(x,odd_arr[j+1])
    y = even_arr[0]
    for j in range(len(even_arr)-1):
        y = math.gcd(y,even_arr[j+1])

    s = True
    if x != 1:
        for j in range(len(even_arr)):
            if even_arr[j] % x == 0:
                s=False
                break
    else:
        s = False

    if s:
        print(x)
        continue
    s = True
    if y != 1:
        for j in range(len(odd_arr)):
            if odd_arr[j] % y == 0:
                s = False
                break
    else:
        s = False
    if s:
        print(y)
    else:
        print(0)

