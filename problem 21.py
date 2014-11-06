def all_divisors(n):
	divisors = []
	for x in range(1,int(n/2+1)):
		if n%x == 0:
			divisors.append(x)
	return divisors

def amicable(upper):
	ami = []
	for x in range(upper):
		divisorsX = all_divisors(x)
		divisorsY = all_divisors(sum(divisorsX))
		if sum(divisorsY) == x and x!=sum(divisorsX):
			ami.append(x)
			ami.append(sum(divisorsY))
	return ami

print (sum(amicable(10000))/2)

input()