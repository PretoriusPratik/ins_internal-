def playfair_prepare(text):
    t, res, i = ''.join(c for c in text.lower() if c.isalpha()).replace('j', 'i'), "", 0
    while i < len(t):
        a, b = t[i], t[i+1] if i+1 < len(t) else 'z'
        res += a + ('x' if a == b else b)
        i += 1 if a == b else 2
    return res

def playfair_matrix(key):
    chars = list(dict.fromkeys(c for c in (key.lower().replace('j', 'i') + "abcdefghiklmnopqrstuvwxyz") if c.isalpha()))
    return [chars[i:i+5] for i in range(0, 25, 5)]

def playfair_pos(M, ch):
    return next((r, c) for r in range(5) for c in range(5) if M[r][c] == ('i' if ch == 'j' else ch))

def playfair_transform(text, M, step=1):
    out = ""
    for i in range(0, len(text), 2):
        (r1, c1), (r2, c2) = playfair_pos(M, text[i]), playfair_pos(M, text[i+1])
        if r1 == r2: out += M[r1][(c1+step)%5] + M[r2][(c2+step)%5]
        elif c1 == c2: out += M[(r1+step)%5][c1] + M[(r2+step)%5][c2]
        else: out += M[r1][c2] + M[r2][c1]
    return out

open("pf_in.txt", "w").write("instruments")
M = playfair_matrix("monarchy")
open("pf_enc.txt", "w").write(playfair_transform(playfair_prepare(open("pf_in.txt").read()), M, 1))

enc = open("pf_enc.txt").read()
print("Ciphertext (from file):", enc)
print("Decrypted :", playfair_transform(enc, M, -1))