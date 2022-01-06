problem_num = int(input())
for problem in range(problem_num):
    string = input()
    if len(string)%2 == 1:
        print('NO')
        continue
    if string[:len(string)//2] == string[len(string)//2:]:
        print('YES')
    else:
        print('NO')