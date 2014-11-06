from collections import Counter

def prvocisla(mez):
    mez +=1
    lst = [True] * mez
    for x in range(2,mez):
        if lst[x]:
            for y in range(2*x,mez,x):
                lst[y] = False
    primes = []
    for x in range(2,mez):
        if lst[x]:
            primes.append(x)
    return primes

def rozklad(n):
    primes = prvocisla(int(n**0.5))
    prvociselnyRozklad = []
    for x in primes:
        while (n%x==0):
            n = n/x
            prvociselnyRozklad.append(x)
    if n != 1:
        prvociselnyRozklad.append(int(n))
    return prvociselnyRozklad

def triangular(n):
    x = 0
    y = 0
    nDivisor = 1
    while nDivisor<n:
        nDivisor = 1
        y+=1
        x+=y
        primes=rozklad(x)
        count = Counter(primes)
        for z in count:
            nDivisor = nDivisor *(count[z]+1)
    return (x)
    

print (triangular(500))


input()