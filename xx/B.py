import math
problem_num = int(input())
for problem in range(problem_num):
    arr = list(map(int,input().split()))
    low,high = arr
    max = 2*10**5
    for i in range(1,18):
        x=high//2**i * 2**i
        xx = low // 2 ** i * 2 ** i
        y = high - x + 1
        z = low -xx
        num0 = x // 2 + y//2**i*2**i + min([y%2**i]) (y % 2 ** i)//2**(i-1) * 2**(i-1)
        num1 = x // 2





