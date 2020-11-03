from itertools import permutations 
from pwn import xor

c = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print(xor(c[:7], b'crypto{'))
# got - > b'myXORke'

print(xor(c, b'myXORkey'))
# got -> b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'