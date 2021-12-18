x, y = map(int, input().split())
bin_x = bin(x)[2:]
bin_y = bin(y)[2:]

lst = [bin_x + '1', bin_x.strip('0')]
flag = False
nxt = False
if bin_x == bin_y:
    print('YES')
    nxt = True
if not nxt:
    for q in lst:
        div = len(bin_y) - len(q) + 1
        for j in range(div):
            if '1' * j + q + '1' * (div-j-1) == bin_y or '1' * j + q[::-1] + '1' * (div-j-1) == bin_y:
                print('YES')
                flag = True
                break
        if flag:
            break
    if not flag:
        print('NO')