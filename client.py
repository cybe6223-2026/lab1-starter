"""
CYBE 6223 — Lab 1: Client
Connect to primary and send SET / GET / DELETE commands.

Usage:
    python3 client.py --host 127.0.0.1 --port 6001
"""

import socket, argparse, uuid

session_id = str(uuid.uuid4())[:8]
seq_no = 0

def send_command(host, port, command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall((command + "\n").encode())
        return s.recv(1024).decode().strip()

def main(host, port):
    global seq_no
    print(f"Connected to {host}:{port}  |  session={session_id}")
    print("Commands: SET <key> <value> | GET <key> | DELETE <key> | quit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not line or line.lower() == "quit":
            break
        parts = line.split()
        if parts[0].upper() in ("SET", "DELETE"):
            seq_no += 1
        cmd = f"{line} {session_id} {seq_no}"
        response = send_command(host, port, cmd)
        print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=6001)
    args = parser.parse_args()
    main(args.host, args.port)
