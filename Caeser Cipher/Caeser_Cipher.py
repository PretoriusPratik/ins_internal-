def caesar(text, key):
    return "".join(chr((ord(c) + key - 32) % 95 + 32) if 32 <= ord(c) <= 126 else c for c in text)

open("caesar_in.txt", "w").write("Hello, World! 123")
key = 5
open("caesar_enc.txt", "w").write(caesar(open("caesar_in.txt").read(), key))

cipher_from_file = open("caesar_enc.txt").read()
print("Ciphertext (from file):", cipher_from_file)
print("Decrypted :", caesar(cipher_from_file, -key))