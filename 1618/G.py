'''미완성'''
n, m, n_q = input().split()
init_a = input().split()
init_b = input().split()
q_lst = input().split()
# n,m,n_1 = '3 4 5'.split()
# init_a = '10 30 15'.split()
# init_b = '12 31 14 18'.split()
# q_lst = '0 1 2 3 4'.split()
init_a = [int(a) for a in init_a]
init_b = [int(b) for b in init_b]
q_lst = [int(q) for q in q_lst]
lst = init_a + init_b
lst.sort(reverse=True)

for q in q_lst:
    if q == 0:
        print(sum(init_a))
        continue
    div = []
    dum = [lst[0]]
    for i in range(len(lst) - 1):
        if lst[i] - lst[i+1] <= q:
            dum.append(lst[i+1])
        else:
            div.append(dum)
            dum = [lst[i+1]]
    div.append(dum)
    dum_a = []
    for i in range(len(init_a)):
        for j in range(len(div)):
            if init_a[i] in div[j]:
                dum_a.append(j)
                break
    div = [div[i][:dum_a.count(i)] for i in range(len(div))]
    s = 0
    for i in range(len(div)):
        s += sum(div[i])
    print(s)

