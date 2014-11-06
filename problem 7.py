def primes(margin):
    lst = [True] * margin
    prvocisla = []
    for x in range(2,margin):
        if lst[x]:
            for y in range(x*2,margin,x):
                lst[y] = False
    for x in range(2,margin):
        if lst[x]:
            prvocisla.append(x)
    return prvocisla[10000]




print (primes(1000000))
input()