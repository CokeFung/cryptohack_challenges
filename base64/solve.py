from base64 import b64encode, b64decode
b64_hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
b64 = b64encode(bytes.fromhex(b64_hex)).decode()


print(b64)