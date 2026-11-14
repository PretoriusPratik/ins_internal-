def row_encrypt(text, cols):
    text += 'X' * ((-len(text)) % cols)
    return ''.join(text[r*cols + c] for c in range(cols) for r in range(len(text)//cols))

def row_decrypt(cipher, cols):
    rows = len(cipher) // cols
    return ''.join(cipher[c*rows + r] for r in range(rows) for c in range(cols)).rstrip('X')

open("row_in.txt", "w").write("HELLOTRANSFORMATION")
open("row_enc.txt", "w").write(row_encrypt(open("row_in.txt").read(), 4))
enc = open("row_enc.txt").read()
print("Encrypted (file):", enc, "| Decrypted:", row_decrypt(enc, 4))