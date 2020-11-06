p = 29
ints = [14, 6, 11]

for i in range(1,p):
	for n in ints:
		if (i**2)%p == n:
			print(i, n)