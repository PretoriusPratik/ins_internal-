import os, ssl, socket, subprocess, tempfile, threading

open("tls_in.txt", "w").write("Hello from TLS client via text file!")
tmpdir = tempfile.mkdtemp()
cert, key = os.path.join(tmpdir, "s.crt"), os.path.join(tmpdir, "s.key")
subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-keyout", key, "-out", cert, "-days", "1", "-nodes", "-subj", "/CN=localhost"], check=True, capture_output=True)

ready, info = threading.Event(), {}
def server():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(cert, key)
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0)); s.listen(1)
        info["port"] = s.getsockname()[1]; ready.set()
        with ctx.wrap_socket(s, server_side=True) as ss:
            conn, _ = ss.accept()
            open("tls_server_recv.txt", "w").write(conn.recv(1024).decode())
            conn.sendall(b"Secure TLS response from server")

threading.Thread(target=server, daemon=True).start(); ready.wait()
c_ctx = ssl._create_unverified_context()
with socket.create_connection(("127.0.0.1", info["port"])) as s, c_ctx.wrap_socket(s, server_hostname="localhost") as ss:
    ss.sendall(open("tls_in.txt", "rb").read())
    print("Server Received (saved to file):", open("tls_server_recv.txt").read() or ss.recv(1024).decode())
    print("Server Saved Payload           :", open("tls_server_recv.txt").read())