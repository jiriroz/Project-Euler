import time

def Main():
	start_time = time.time()
	powers = []
	for a in range(2,101):
		for b in range(2,101):
			pow = a**b
			if pow not in powers:
				powers.append(pow)
	print (len(powers))



	print (str(time.time()-start_time)+' seconds')

if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()