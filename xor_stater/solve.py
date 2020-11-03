s = "label"

flag = ""
for i in s:
	flag += chr(ord(i) ^ 13)
print("crypto{%s}" % flag)

