def factorial(n):
    f = 1
    while n>0:
        f = f*n
        n-=1
    return f

x = factorial(100)

sum = 0
for y in (str(x)):
    sum +=int(y)

print (sum)
input()