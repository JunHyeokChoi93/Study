problem_num = int(input())
for i in range(problem_num):
    nums = input().split()
    nums = [int(i) for i in nums]
    a,b = nums[:2]
    c = nums[-1]-a-b
    print('{} {} {}'.format(a,b,c))
