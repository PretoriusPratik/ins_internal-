def rail_fence_encrypt(text, rails):
    rows, r, d = [''] * rails, 0, 1
    for ch in text:
        rows[r] += ch
        if r in (0, rails - 1): d = 1 if r == 0 else -1
        r += d
    return ''.join(rows)

def rail_fence_decrypt(cipher, rails):
    pat, r, d = [[False]*len(cipher) for _ in range(rails)], 0, 1
    for c in range(len(cipher)):
        pat[r][c] = True
        if r in (0, rails - 1): d = 1 if r == 0 else -1
        r += d
    grid, k = [[''] * len(cipher) for _ in range(rails)], 0
    for r in range(rails):
        for c in range(len(cipher)):
            if pat[r][c]:
                grid[r][c] = cipher[k]
                k += 1
    res, r, d = "", 0, 1
    for c in range(len(cipher)):
        res += grid[r][c]
        if r in (0, rails - 1): d = 1 if r == 0 else -1
        r += d
    return res

open("rf_in.txt", "w").write("WEAREDISCOVEREDFLEEATONCE")
open("rf_enc.txt", "w").write(rail_fence_encrypt(open("rf_in.txt").read(), 3))
enc = open("rf_enc.txt").read()
print("Encrypted (file):", enc, "| Decrypted:", rail_fence_decrypt(enc, 3))