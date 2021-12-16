problem_num = int(input())
for i in range(problem_num):
    num = int(input())
    bigrams = input().split()
    fst = [aa[0] for aa in bigrams]
    snd = [aa[1] for aa in bigrams]
    final = [fst[0]]
    flag = True
    for i in range(len(fst)-1):
        if fst[i+1] == snd[i]:
            final.append(fst[i+1])
        elif fst[i+1] != snd[i]:
            final.append(snd[i])
            final.append(fst[i+1])
            flag = False
    final.append(snd[-1])

    if flag:
        final.append(final[-1])
    final = ''.join(final)
    print(final)



