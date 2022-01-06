problem_num = int(input())
def sum(n1,n2):
    return_str = ''
    n1 = n1.zfill(len(n2))
    n2 = n1.zfill(len(n1))
    for i in range(len(n1)):
        return_str = str(int(n1[i])+int(n2[i])) + return_str
    return return_str
for problem in range(problem_num):
    n1,s = input().split()
    n1 = n1.zfill(len(s))
    n1_idx = -1
    s_idx = -1
    n2 = ''
    flag = True
    while s_idx >= -len(s):
        if int(n1[n1_idx]) > int(s[s_idx]) and s_idx!=-len(s):
            if s_idx == -1:
                sum_s = int(s[s_idx-1:])
            else:
                sum_s = int(s[s_idx-1:s_idx+1])
            if sum_s >= 20:
                flag = False
                break
            else:
                n2 = n2 + str(int(sum_s) - int(n1[n1_idx]))
                s_idx -= 2
                n1_idx -= 1

        else:
            sum_s = int(s[s_idx])
            n2 = n2 + str(int(sum_s) - int(n1[n1_idx]))
            s_idx -= 1
            n1_idx -= 1
    n2 = n2[::-1]
    ans = sum(n1,n2)
    if ans != s:
        flag = False
    if flag:
        print(n2)
    else:
        print(-1)

