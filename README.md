# CYBE 6223 · Lab 1 — Replicated Key-Value Store
**MSc Cybersecurity · University of Bamenda · AY 2025–26**

**Deadline: Thursday 7 May 2026 · 17:00**

---

## Overview
Build a primary-backup replicated key-value store in Python using TCP sockets.
The lab has three stages, each adding a consistency guarantee.

| Stage | Task | Time |
|-------|------|------|
| 1 | Primary-backup KV store with synchronous replication | 30–40 min |
| 2 | Failure detection and automatic failover | 30–35 min |
| 3 | Read-your-writes session guarantee + latency measurement | 20–25 min |

## Running the system

```bash
# Terminal 1 — Primary
./run_primary.sh

# Terminal 2 — Backup 1
./run_backup.sh 6002

# Terminal 3 — Backup 2
./run_backup.sh 6003

# Terminal 4 — Client
python3 client.py --port 6001

# Stage 2 — Kill the primary
./tests/kill_primary.sh
```

## Submission
1. Push all code to this repository before the deadline.
2. Export your report as `report/report.pdf` (max 4 pages, appendix excluded).
3. Use `report/REPORT_TEMPLATE.md` as your starting point.

Late penalty: −5% per 24 hours.
