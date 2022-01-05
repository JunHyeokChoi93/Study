problem_num = int(input())
def cost_calc(c_lst,idx_r,idx_l):
    if idx_r == idx_l:
        cost = c_lst[idx_r]
    else:
        cost = c_lst[idx_r] + c_lst[idx_l]
    return cost
for problem in range(problem_num):
    n = int(input())
    r_lst = []
    l_lst = []
    c_lst = []
    for nn in range(n):
        r,l,c = map(int,input().split())
        r_lst.append(r);l_lst.append(l),c_lst.append(c)
        min_r = min(r_lst);max_l = max(l_lst)
        min_r_cost = 10**9+1;min_l_cost=10**9+1
        min_r_idx = -1
        min_l_idx = -1
        for i in range(len(c_lst)):
            if r_lst[i] == min_r:
                if min_r_cost >= c_lst[i]:
                    min_r_idx = i
                    min_r_cost = c_lst[i]
            if l_lst[i] == max_l:
                if min_l_cost >= c_lst[i]:
                    min_l_idx = i
                    min_l_cost = c_lst[i]
        if min_r_idx == min_l_idx:
            print(c_lst[min_l_idx])
            r_lst = [r_lst[min_r_idx]]
            l_lst = [l_lst[min_r_idx]]
            c_lst = [c_lst[min_r_idx]]

        else:
            if l_lst[min_r_idx] == l_lst[min_l_idx]:
                print(c_lst[min_r_idx])
                r_lst = [r_lst[min_r_idx]]
                l_lst = [l_lst[min_r_idx]]
                c_lst = [c_lst[min_r_idx]]
            elif r_lst[min_l_idx] == r_lst[min_r_idx]:
                print(c_lst[min_l_idx])
                r_lst = [r_lst[min_l_idx]]
                l_lst = [l_lst[min_l_idx]]
                c_lst = [c_lst[min_l_idx]]
            else:
                print(c_lst[min_r_idx]+c_lst[min_l_idx])
                r_lst = [r_lst[min_r_idx],r_lst[min_l_idx]]
                l_lst = [l_lst[min_r_idx],l_lst[min_l_idx]]
                c_lst = [c_lst[min_r_idx],c_lst[min_l_idx]]