from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Create two input .txt files: one for key, one for encrypted hex text
open("des_key.txt", "wb").write(b"8bytekey")
key = open("des_key.txt", "rb").read().strip()

cipher_bytes = DES.new(key, DES.MODE_ECB).encrypt(pad(b"Hello, this is a secret message!", 8))
open("des_cipher.txt", "w").write(binascii.hexlify(cipher_bytes).decode())

# Read from the two .txt files (des_cipher.txt & des_key.txt) and decrypt
loaded_key = open("des_key.txt", "rb").read().strip()
loaded_cipher = binascii.unhexlify(open("des_cipher.txt").read().strip())
decrypted = unpad(DES.new(loaded_key, DES.MODE_ECB).decrypt(loaded_cipher), 8).decode()

print("Encrypted Hex (from des_cipher.txt):", open("des_cipher.txt").read())
print("Decrypted (using des_key.txt)      :", decrypted)