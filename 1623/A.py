problem_num = int(input())
def return_count(s,b,d):
    if b-d>0:
        return_value = 2*(s-b) + b - d
    else:
        return_value = d-b
    return return_value
for problem in range(problem_num):
    n,m,rb,cb,rd,cd = map(int,input().split())
    print(min(return_count(n,rb,rd),return_count(m,cb,cd)))

