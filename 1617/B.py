import math
def find_div(num):
    for i in range(num//2,1,-1):
        if math.gcd(i,num-i) == 1:
            return i
problem_num = int(input())
for i in range(problem_num):
    S = int(input())
    c = 1
    a = find_div(S-1)
    b = S - 1 - a
    print(a,b,c)


