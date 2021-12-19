'''미완성'''
n, m, n_q = input().split()
init_a = input().split()
init_b = input().split()
q_lst = input().split()
# n,m,n_1 = '345'
# init_a = '10 30 15'.split()
# init_b = '12 31 14 18'.split()
# q_lst = '0 1 2 3 4'.split()
init_a = [int(a) for a in init_a]
init_b = [int(b) for b in init_b]
q_lst = [int(q) for q in q_lst]
init_a.sort(reverse=True)
init_b.sort(reverse=True)
stor_a = init_a.copy()
stor_b = init_b.copy()


def find_max(a, b_lst, q):
    init_a = a
    if max(b_lst) > a:
        ran = range(a + q, a, -1)
        dum_b = [b for b in b_lst]
        for i in range(len(dum_b)-1,-1,-1):
            if dum_b[i] in ran:
                dum, a = find_max(dum_b[i], b_lst, q)
                break
    return init_a, a


for q in q_lst:
    init_a = stor_a.copy()
    init_b = stor_b.copy()
    if q == 0:
        print(sum(init_a))
        continue

    for i in range(len(init_a)):
        ai = init_a[i]
        x, bi = find_max(ai, init_b, q)
        if x != bi:
            init_b[init_b.index(bi)] = x
            init_a[i] = bi
    print(sum(init_a))