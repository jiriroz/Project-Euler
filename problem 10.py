def prvocisla(mez):
    list = [True] * mez
    for x in range(2,mez):
        if list[x]:
            for y in range(x*2,mez,x):
                list[y] = False
    prvocisla = []
    for x in range(2,mez):
        if list[x]:
            prvocisla.append(x)
    return sum(prvocisla)
    
print (prvocisla(2000000))

input()