import math

def sito(do):
  do += 1
  sito = [True] * do
 
  for i in range(2, do):
    if sito[i]:
      for j in range(i*2, do, i):
        sito[j]=False
 
  prvocisla=[]
  for i in range(2, do):
    if sito[i]:
      prvocisla.append(i)
  return prvocisla
  
def rozklad(x):
    prvocisla = sito(int(math.sqrt(x)))
    rozklad = []
    for y in prvocisla:
        while x%y == 0:
            x = x/y
            rozklad.append(y)
    return rozklad

print (rozklad(600851475143))

input()