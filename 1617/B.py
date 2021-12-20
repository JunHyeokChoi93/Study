def divisor_find(num):
    for i in range(6,num):
        if num % i == 0:
            return i
        else:
            continue
    return None

problem_num = int(input())
for i in range(problem_num):
    S = int(input())
    c = divisor_find(S)

