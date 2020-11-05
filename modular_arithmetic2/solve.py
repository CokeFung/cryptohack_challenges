def solv(n, m):
	if m == 1:
		return n

def main():
	p = 65537
	n = 273246787654
	m = 65536
	print(pow(n,m)%p)

main()