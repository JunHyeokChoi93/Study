problem_num = int(input())
for problem in range(problem_num):
    n = int(input())
    lst = []
    len_count = []
    n_lst = list(range(1,n+1))
    for i in range(n):
        l,r = map(int,input().split())
        lst.append(list(range(l,r+1)))
    lst2 = lst.copy()



