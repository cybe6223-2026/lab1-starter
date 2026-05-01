#!/bin/bash
# Usage: ./run_backup.sh 6002
# Start a backup node on the given port
python3 server.py --role backup --port "${1:-6002}"
