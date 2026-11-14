import random, math

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def gen_6digit_prime():
    while not is_prime(p := random.randint(100000, 999999)): pass
    return p

p, q = gen_6digit_prime(), gen_6digit_prime()
n, phi = p * q, (p - 1) * (q - 1)
e = 65537
while math.gcd(e, phi) != 1: e += 2
d = pow(e, -1, phi)

open("rsa_msg.txt", "w").write("Secret RSA Lab Message")
msg = open("rsa_msg.txt").read()

# Encrypt message from file into rsa_enc.txt
open("rsa_enc.txt", "w").write(" ".join(str(pow(ord(c), e, n)) for c in msg))

# Read encrypted blocks from rsa_enc.txt and decrypt
cipher_blocks = list(map(int, open("rsa_enc.txt").read().split()))
decrypted = "".join(chr(pow(c, d, n)) for c in cipher_blocks)

print(f"6-Digit Primes: p={p}, q={q} | Modulus n={n}")
print("Encrypted (from file):", cipher_blocks[:5], "...")
print("Decrypted            :", decrypted)