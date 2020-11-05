#Python program for Extended Euclidean algorithm
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)

gcd, x, y = egcd(26513, 32321)
print("nactf{%d,%d}" % (x, y))