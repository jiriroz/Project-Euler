def sequence(x,count):
    count +=1
    if x == 1:
        lst.append(count)
        return
    elif x%2 == 0:
        x = x/2
    else:
        x = 3*x + 1
    sequence(x,count)

global lst
lst = []

for y in range(1,1000000):
    sequence(y,0)
print (lst.index(max(lst))+1)
input()