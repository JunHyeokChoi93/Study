problem_num = int(input())
for i in range(problem_num):
    days = int(input())
    x = input()
    day_info = x.split()
    prev = None
    h = 1
    for d in range(days):
        cur = day_info[d]
        if cur == '0':
            if prev == '0':
                h = -1
                break
            else:
                pass
        elif cur == '1':
            if prev != '1':
                h += 1
            else:
                h += 5
        prev = cur
    print(h)


