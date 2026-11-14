import hashlib, math

p, q, g, x, k = 23, 11, 2, 3, 2
y = pow(g, x, p)
dsa_hash = lambda m: int(hashlib.sha256(m.encode()).hexdigest(), 16) % q

open("dsa_msg.txt", "w").write("Digital Signature")
z = dsa_hash(open("dsa_msg.txt").read())
r = pow(g, k, p) % q
s = (pow(k, -1, q) * (z + x * r)) % q
open("dsa_sig.txt", "w").write(f"{r} {s}")

# Read message and signature from .txt files to verify
msg_in = open("dsa_msg.txt").read()
r_in, s_in = map(int, open("dsa_sig.txt").read().split())
w = pow(s_in, -1, q)
v = (pow(g, (dsa_hash(msg_in)*w)%q, p) * pow(y, (r_in*w)%q, p) % p) % q
print(f"Msg (file): {msg_in} | Sig (file): {(r_in, s_in)} | Verified: {v == r_in}")