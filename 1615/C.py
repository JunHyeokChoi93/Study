problem_num = int(input())
for i in range(problem_num):
    n = int(input())
    arr1 = input()
    arr2 = input()
    if arr2.count('1') not in [arr1.count('1'),n-arr1.count('1')+1]:
        print(-1)
        continue
    # same_0 = 0
    # same_1 = 0
    # diff_0 = 0
    # diff_1 = 0
    same = 0
    diff = 0
    for j in range(len(arr1)):
        if arr1[j] == arr2[j]:
            same += 1
        else:
            diff += 1
    if arr1.count('1') == n-arr1.count('1')+1:
        print(min([same,diff]))
    elif arr2.count('1') == arr1.count('1'):
        print(diff)
    else:
        print(same)
