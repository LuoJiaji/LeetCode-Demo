
N = 1
while N < 400:
    if N > 11 and len(str(N)) % 2 == 0:
        N = 10 ** len(str(N)) + 1

    else:
        N += 1

    print(N)
    