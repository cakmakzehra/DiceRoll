import random

def dice(value):
	for i in range(value):
		print(random.choice(["1","2","3","4","5","6"]), end=" ")
