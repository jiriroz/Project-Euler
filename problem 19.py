years = []
days = []
daycount = []
months = [31,28,31,30,31,30,31,31,30,31,30,31]

count = 0
for year in range(1900,2001):
	if (year%4 == 0):
		if year%100 == 0 and year%400 != 0:
			yrlen = 365
		else:
			yrlen = 366
	else:
		yrlen = 365
	for day in range(1,yrlen+1):
		count +=1
		years.append(year)
		days.append(day)
		daycount.append(count)

firstsundays = 0
curmon = 1
for x in range(365,len(daycount)):
	months[1]=28
	if (years[x]%4 == 0):
		if years[x]%100 == 0 and years[x]%400 != 0:
			months[1]=28
		else:
			months[1]=29
	if days[x]==1: #novy rok
		curmon = 1
	if (days[x] == sum(months[:curmon])+1 or days[x]==1) and (daycount[x]%7 == 0): #testuje prvni den v mesici
		firstsundays+=1
	if (days[x] > sum(months[:curmon])): #novy mesic
		curmon += 1
print (firstsundays)
input()