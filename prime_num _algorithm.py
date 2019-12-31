import math

while True:
	num_str = input('Numbers to check: ')
	if num_str.isdigit():
		num = int(num_str)
		break
		
primes = [1]

for n in range (2,num):
	prime = True
	for i in primes:
		if i >= int(math.sqrt(n)): #because highest possible factor of prime is lower than the square root of itself
			break			
		elif n%i == 0:
			prime = False
			break
	if prime == True:
		print(n)
		primes.append(n)

