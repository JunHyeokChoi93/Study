import sys
problem_num = int(input())
for problem in range(problem_num):
    n = int(input())
    prev = None
    arr = [-1]*n
    judge_arr = [-1] * n
    for i in range(n):
        a,b,c = i, i+1, i+2
        if a <= 0:
            a -= 1
        elif c > n:
            c=1
        a = a%(n+1);b = b%(n+1);c = c%(n+1)
        print('?',a,b,c)
        cur = int(input())
        judge_arr[i] = cur
        if prev != None:
            if prev != cur:
                break
            prev = cur
    if prev ==



    print_line = []
    for i in range(n):
        if arr[i] == 0:
            print_line.append('{}'.format(i+1))
    # print_line = ' '.join(print_line)

    print('!',len(print_line),' '.join(print_line))
    sys.stdout.flush()




