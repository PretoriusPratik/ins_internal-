from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

open("aes_key.txt", "wb").write(b"1234567890123456")
key = open("aes_key.txt", "rb").read().strip()

enc = AES.new(key, AES.MODE_ECB).encrypt(pad(b"Hello, this is a secret message!", 16))
open("aes_cipher.txt", "w").write(binascii.hexlify(enc).decode())

# Read encrypted hex and key from .txt files and decrypt
loaded_key = open("aes_key.txt", "rb").read().strip()
loaded_cipher = binascii.unhexlify(open("aes_cipher.txt").read().strip())
print("Encrypted (from file):", open("aes_cipher.txt").read())
print("Decrypted            :", unpad(AES.new(loaded_key, AES.MODE_ECB).decrypt(loaded_cipher), 16).decode())