#!/bin/bash
# Stage 2 failure experiment — kills the primary process
# Run this after starting primary and both backups
PID=$(lsof -ti tcp:6001)
if [ -z "$PID" ]; then
    echo "No process found on port 6001"
else
    echo "Killing primary (PID $PID) on port 6001..."
    kill -9 $PID
    echo "Done. Watch backup 6002 detect the failure and promote."
fi
