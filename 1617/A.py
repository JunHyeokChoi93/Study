problem_num = int(input())
for i in range(problem_num):
    S = input()
    T = input()
    if T=='abc' and 'a' in S and 'b' in S and 'c' in S:
        S = ''.join(sorted(S))
        b=S.count('b')
        c=S.count('c')
        if len(S) > S.index('c') + c:
            S = S[:S.index('b')] + 'c' * c + 'b' * b + S[S.index('c') + c:]

        else:
            S = S[:S.index('b')] + 'c' * c + 'b' * b
        print(S)

    else:
        print(''.join(sorted(S)))