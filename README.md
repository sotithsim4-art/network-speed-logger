# Network Speed Logger

A Python automation tool that tests your internet speed and logs the results to a file over time.

## What it does
- Tests download speed, upload speed, and ping
- Logs every result with a timestamp to a text file
- Lets you view your full speed history

## Requirements

Install the required library:

```
python -m pip install speedtest-cli
```

## How to run

```
python network_speed.py
```

## Example output

```
Network Speed Logger
--------------------
1. Run speed test
2. View log

Choose an option: 1
Testing network speed... please wait.

Result logged:
  [2026-06-25 23:01:44]  Download: 245.3 Mbps  |  Upload: 18.7 Mbps  |  Ping: 14.2 ms
```

## Why this matters

Network performance monitoring is a key skill in cybersecurity and IT operations. Sudden drops in speed can indicate network attacks, bandwidth abuse, or infrastructure issues.
