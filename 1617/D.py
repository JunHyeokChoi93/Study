import sys
problem_num = int(input())
for problem in range(problem_num):
    n = int(input())
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
    for i in range(n):
        diff = judge_arr[i-1] - judge_arr[i]
        if diff == 1:
            arr[i - 2] = 1
            arr[i - 1] = 1
            arr[(i + 2)%(n+1)] = 0
        elif diff == -1:
            arr[i - 2] = 0
            arr[i - 1] = 0
            arr[(i + 2)%n] = 1
    for i in range(n):
        if arr[i] == -1:
            j = i -1
            if arr[j] == -1:
                continue
            if j == 0:
                judge_sub = [judge_arr[-1], judge_arr[0], judge_arr[1]]
            elif j == - 1:
                judge_sub = [judge_arr[-2], judge_arr[-1], judge_arr[0]]
            else:
                judge_sub = judge_arr[j - 1:j + 2]
            i1,i2,i3,i4 = j-2,j-1,(j+1)%n,(j+2)%n
            if arr[j] == 0:
                if judge_sub == [1,1,1]:
                    arr[i1] = 1;arr[i2] = 1;arr[i3] = 1;arr[i4] = 1
                elif judge_sub == [0,1,0]:
                    arr[i1] = 0;arr[i2] = 1;arr[i3] = 1;arr[i4] = 0
                elif judge_sub == [1,1,0]:
                    arr[i1] = 1;arr[j-1] = 1;arr[i3] = 1;arr[i4] = 0
                elif judge_sub == [0,1,1]:
                    arr[i1] = 1;arr[i2] = 0;arr[i3] = 0;arr[i4] = 0
                elif judge_sub == [0,0,1]:
                    arr[i2] = 0;arr[i3] = 1;arr[i4] = 1
                elif judge_sub == [1,0,0]:
                    arr[i1] = 1;arr[i2] = 1;arr[i3] = 0

            elif arr[j] == 1:
                if judge_sub == [0,0,0]:
                    arr[i1] = 0;arr[i2] = 0;arr[i3] = 0;arr[i4] = 0
                elif judge_sub == [1,0,1]:
                    arr[i1] = 1;arr[i2] = 0;arr[i3] = 0;arr[i4] = 1
                elif judge_sub == [0,0,1]:
                    arr[i1] = 0;arr[i2] = 0;arr[i3] = 0;arr[i4] = 1
                elif judge_sub == [1,0,0]:
                    arr[i1] = 0;arr[i2] = 1;arr[i3] = 1;arr[i4] = 1
                elif judge_sub == [1,1,0]:
                    arr[i2] = 1;arr[i3] = 0;arr[i4] = 0
                elif judge_sub == [0,1,1]:
                    arr[i1] = 0;arr[i2] = 0;arr[i3] = 1

    print_line = []
    for i in range(n):
        if arr[i] == 0:
            print_line.append('{}'.format(i+1))
    # print_line = ' '.join(print_line)

    print('!',len(print_line),' '.join(print_line))
    sys.stdout.flush()




