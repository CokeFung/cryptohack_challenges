from pwn import * # pip install pwntools
import json
import codecs
import base64

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def solve(typee, encoded):
	if typee == "rot13":
		return codecs.decode(encoded, 'rot13')
	if typee == "utf-8":
		return "".join([chr(i) for i in encoded])
	if typee == "base64":
		return base64.b64decode(encoded.encode()).decode()
	if typee == "hex":
		return bytes.fromhex(encoded).decode()
	if typee == "bigint":
		return bytes.fromhex(encoded[2:]).decode()
	return ""

def main():
	received = json_recv()

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	to_send = {
	    "decoded": solve(received["type"], received["encoded"])
	}
	json_send(to_send)
	

for i in range(100):
	main()
json_recv()

