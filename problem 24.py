import time
import math
start_time = time.time()

def fact(target,result):
	numbers = [x for x in range(10) if str(x) not in result]
	if len(numbers)==0:
		return result
	n = math.factorial(len(numbers)-1)
	index = int(math.ceil(target/n)-1)
	result += str(numbers[index])
	target = target - index*n
	return fact(target,result)

print (fact(1000000,''))

print (str(time.time()-start_time)+' seconds')
input()