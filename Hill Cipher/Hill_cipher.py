import numpy as np

def mod_matrix_inverse(K, mod=26):
    n = len(K)
    det_inv = pow(int(round(np.linalg.det(K))) % mod, -1, mod)
    cof = [[((-1)**(r+c)) * int(round(np.linalg.det(np.delete(np.delete(K, r, 0), c, 1)))) for c in range(n)] for r in range(n)]
    return (det_inv * np.array(cof).T) % mod

def hill_transform(text, K):
    n = len(K)
    t = ''.join(c for c in text.upper() if c.isalpha())
    t += 'X' * ((-len(t)) % n)
    return ''.join(chr(int(x)+65) for i in range(0, len(t), n) for x in K.dot([ord(c)-65 for c in t[i:i+n]]) % 26)

# Dynamic Key Sizes (2x2 and 3x3) and Variable Message Lengths via .txt files
tests = [
    ("3 3\n2 5", "ACT", "2x2 Short"),
    ("6 24 1\n13 16 10\n20 17 15", "DYNAMICMESSAGELENGTHFORHILLCIPHER", "3x3 Long")
]
for k_str, msg, label in tests:
    open("hill_key.txt", "w").write(k_str)
    open("hill_msg.txt", "w").write(msg)
    
    K = np.array([list(map(int, line.split())) for line in open("hill_key.txt").read().splitlines()])
    open("hill_enc.txt", "w").write(hill_transform(open("hill_msg.txt").read(), K))
    
    enc = open("hill_enc.txt").read()
    print(f"[{label}] Cipher (file): {enc} | Decrypted: {hill_transform(enc, mod_matrix_inverse(K))}")