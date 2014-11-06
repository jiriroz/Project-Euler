def palindrome():
    lst = []
    for x in range(100,999):
        for y in range(100,999):
            z = x*y
            a = str(z)
            if a == a[::-1]:
                lst.append(z)
    return max(lst)
            

print (palindrome())
input()

