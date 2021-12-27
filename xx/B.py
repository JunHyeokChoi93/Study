import math
problem_num = int(input())
for problem in range(problem_num):
    arr = list(map(int,input().split()))
    low,high = arr
    num_0_lst = []
    num_1_lst = []
    ran = int(math.log2(high))
    for i in range(0,ran + 1):
        x = high//2**(i+1) * 2**(i+1) - 1
        y = low // 2 ** (i+1) * 2 ** (i+1)

        length = x - y + 1
        count_0 = length // 2
        count_1 = length // 2

        count_to_high = high - x
        count_to_low = low - y
        if count_to_high // 2 ** i >= 1:
            count_0 += 2 ** i
            count_1 += count_to_high % 2 ** i
        else:
            count_0 += count_to_high

        if count_to_low // 2 ** i >= 1:
            count_0 -= 2 ** i
            count_1 -= count_to_low % 2 ** i
        else:
            count_0 -= count_to_low
        num_0_lst.append(count_0)
        num_1_lst.append(count_1)

    # print(min(num_0_lst + num_1_lst))
    print(min(num_0_lst))



