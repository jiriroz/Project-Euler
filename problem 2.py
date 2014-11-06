a = 0
b = 1
fib = []

while b<4000000:
    a+=b
    b+=a
    if a%2 ==0:
        fib.append(a)
    elif b%2 ==0:
        fib.append(b)

print (sum(fib))
input()