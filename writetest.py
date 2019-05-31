import random

k = 0
sum = 1000
for i in range(sum):
	a1 = random.randint(1800,2000)
	a2 = random.randint(1800,2000)
	if abs(a1-a2)<20:
		k +=1


print(k/sum)