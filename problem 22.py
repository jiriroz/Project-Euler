import string
import re

file = open('names.txt','r')
names = file.read()
file.close()
alphabet = string.ascii_uppercase
names = re.sub('"','',names)
names = names.split(',')

namenums = []
for x in names:
	letters = []
	for y in range(len(x)):
		letters.append(alphabet.index(x[y])+1)
	namenums.append(letters)

def sort(list):
	sorted = [list[0],[28]]
	for x in range(1,len(list)):
		for y in range(len(sorted)):
			if compare(list[x],sorted[y]):
				sorted.insert(y,list[x])
				break
	return sorted[:len(sorted)-1]

def compare(word1,word2):
	if word1 == word2:
		return True
	if word1[0]<word2[0]:
		return True
	elif word1[0]>word2[0]:
		return False
	if len(word1)==1 and len(word2) > 1:
		return True
	elif len(word2)==1 and len(word1) > 1:
		return False
	word1 = word1[1:]
	word2 = word2[1:]
	return compare(word1,word2)
sortedlist = sort(namenums)
print ('done sorting')

score = 0
for x in range(len(sortedlist)):
	score += sum(sortedlist[x])*(x+1)
print (score)



input()