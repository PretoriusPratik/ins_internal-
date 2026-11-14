import hashlib

open("sha_in.txt", "w").write("Data and Network Security Lab")
msg = open("sha_in.txt").read()
open("sha_out.txt", "w").write(hashlib.sha256(msg.encode()).hexdigest())

digest = open("sha_out.txt").read()
print("Message (from file):", msg)
print("SHA-256 (from file):", digest, f"({len(digest)} hex chars)")