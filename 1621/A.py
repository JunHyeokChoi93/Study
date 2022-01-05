problem_num = int(input())
for problem in range(problem_num):
    n,k = map(int,input().split())
    if n // 2 + n % 2 < k:
        print(-1)
    else:
        num_rook = 0
        for i in range(n):
            if i % 2 == 0 and num_rook < k:
                print_ln = '.' * i + 'R' + '.' * (n-i-1)
                num_rook += 1
                print(print_ln)
            else:
                print_ln = '.' * n
                print(print_ln)