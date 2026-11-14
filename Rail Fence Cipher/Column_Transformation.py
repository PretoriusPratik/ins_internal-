def col_encrypt(text, key):
    cols = len(key)
    text += 'X' * ((-len(text)) % cols)
    order = sorted(range(cols), key=lambda i: (key[i], i))
    return ''.join(text[r*cols + c] for c in order for r in range(len(text)//cols))

def col_decrypt(cipher, key):
    cols, rows = len(key), len(cipher) // len(key)
    order = sorted(range(cols), key=lambda i: (key[i], i))
    mat, k = [['']*cols for _ in range(rows)], 0
    for c in order:
        for r in range(rows): mat[r][c], k = cipher[k], k + 1
    return ''.join(''.join(r) for r in mat).rstrip('X')

open("col_in.txt", "w").write("WEAREDISCOVERED")
open("col_enc.txt", "w").write(col_encrypt(open("col_in.txt").read(), "ZEBRA"))
enc = open("col_enc.txt").read()
print("Encrypted (file):", enc, "| Decrypted:", col_decrypt(enc, "ZEBRA"))