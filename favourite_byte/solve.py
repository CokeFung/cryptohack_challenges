from pwn import xor

c = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for i in range(1,256):
	tmp = xor(c, i)
	if b'crypto' in tmp:
		print(tmp.decode())
		break