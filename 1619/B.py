problem_num = int(input())
for problem in range(problem_num):
    number = int(input())

    square = int(number**(1/2))+1
    third = int(number**(1/3))+1
    if square ** 2 > number:
        square = square - 2
    else:
        square = square - 1
    if third ** 3 > number:
        third = third - 2
    else:
        third = third - 1
    sixth = int(number**(1/6))+1
    if sixth ** 6 > number:
        sixth = sixth - 2
    else:
        sixth = sixth - 1
    count = square + third + 1 - sixth
    print(count)
