"""
CYBE 6223 — Lab 1: Replicated Key-Value Store
University of Bamenda · MSc Cybersecurity · AY 2025–26

Deadline: Thursday 7 May 2026 · 17:00
Submission: GitHub repo (this repo) + PDF report ≤ 4 pages

Usage:
    python3 server.py --role primary  --port 6001
    python3 server.py --role backup   --port 6002
    python3 server.py --role backup   --port 6003
"""

import socket, threading, argparse, time

# ── Configuration ──────────────────────────────────────────────────────
BACKUP_ADDRS = [("127.0.0.1", 6002), ("127.0.0.1", 6003)]
HEARTBEAT_INTERVAL = 0.5   # seconds
HEARTBEAT_TIMEOUT  = 1.0   # seconds
MISS_THRESHOLD     = 3     # missed heartbeats before failover

store = {}          # the key-value store
role  = "primary"   # "primary" or "backup"

# ── TODO Stage 1: Replication ──────────────────────────────────────────
def replicate(command, key, value=None):
    """
    Send a REPLICATE command to all backup nodes.
    Wait for OK from each before returning.
    Return True if all ACKed, False otherwise.
    """
    # TODO: implement
    pass

# ── TODO Stage 1: Client handler ───────────────────────────────────────
def handle_client(conn, addr):
    """
    Parse SET / GET / DELETE commands from a client.
    For writes: replicate first, then ACK.
    For reads: return local value immediately.
    """
    # TODO: implement
    pass

# ── TODO Stage 2: Heartbeat sender (primary → backups) ─────────────────
def heartbeat_sender():
    """
    Send HEARTBEAT to each backup every HEARTBEAT_INTERVAL seconds.
    Track consecutive failures. Log unavailable backups.
    """
    # TODO: implement
    pass

# ── TODO Stage 2: Heartbeat watcher (backup → primary) ─────────────────
def heartbeat_watcher(primary_port):
    """
    Ping the primary every HEARTBEAT_INTERVAL seconds.
    If MISS_THRESHOLD missed: call promote_to_primary().
    """
    # TODO: implement
    pass

# ── TODO Stage 2: Promotion ────────────────────────────────────────────
def promote_to_primary():
    """
    Declare this backup as the new primary.
    Begin accepting client writes.
    Election rule: lowest port number wins.
    """
    # TODO: implement
    pass

# ── TODO Stage 3: Session guarantee ────────────────────────────────────
def check_session(session_id, seq_no, key):
    """
    Verify this replica has applied the write at (session_id, seq_no).
    If not, fetch current value from primary before responding.
    Return the correct value.
    """
    # TODO: implement
    pass

# ── Server entry point ─────────────────────────────────────────────────
def start_server(port):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(10)
    print(f"[{role.upper()}] Listening on port {port}")
    while True:
        conn, addr = srv.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=["primary", "backup"], required=True)
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()
    role = args.role
    if role == "primary":
        threading.Thread(target=heartbeat_sender, daemon=True).start()
    else:
        threading.Thread(target=heartbeat_watcher, args=(6001,), daemon=True).start()
    start_server(args.port)
