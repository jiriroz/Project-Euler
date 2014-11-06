def pythagorean():
    for x in range(1,999):
        for y in range(1,999):
            z = x**2 + y**2
            if (z**0.5 == int(z**0.5)) and (x+y+z**0.5 ==1000):
                print (x,y,int(z**0.5))

print (pythagorean())

input()