# mynmap.py

## Overview
`mynmap.py` is a simple Python-based port scanner that allows you to scan TCP and UDP ports on a target host. It provides basic functionality to determine whether specific ports are open, closed, or filtered. This tool is lightweight, easy to use, and designed for educational or personal use.

## Features
- Scans TCP ports to check if they are open.
- Scans UDP ports to check if they are open or filtered.
- Accepts a range of ports or individual ports to scan.
- Command-line interface for flexibility and ease of use.

## Usage
Run the script using the following command:
```bash
python3 mynmap.py <target> -p <ports> [options]
```

### Arguments
- **`<target>`**: The IP address or hostname of the target to scan.
- **`-p/--ports`**: Ports to scan. This can be:
  - A single port (e.g., `80`)
  - A range of ports (e.g., `20-25`)
  - A comma-separated list of ports (e.g., `80,443,8080`)

### Options
- **`-sT`**: Perform a TCP scan.
- **`-sU`**: Perform a UDP scan.

### Examples
1. Scan TCP ports 20-25 on a target:
   ```bash
   python3 mynmap.py 192.168.1.1 -p 20-25 -sT
   ```
2. Scan UDP ports 53 and 123 on a target:
   ```bash
   python3 mynmap.py example.com -p 53,123 -sU
   ```
3. Perform both TCP and UDP scans on ports 80 and 443:
   ```bash
   python3 mynmap.py 10.0.0.1 -p 80,443 -sT -sU
   ```

## How It Works
1. **TCP Scan (`-sT`)**:
   - Attempts to establish a connection to each specified port.
   - Reports if the port is open or closed.
2. **UDP Scan (`-sU`)**:
   - Sends an empty packet to each specified port and waits for a response.
   - Reports if the port is open, filtered, or non-responsive.

## Limitations
- UDP scans may report ports as "filtered" if no response is received. This is due to how UDP handles communication (lack of acknowledgment).
- Requires appropriate permissions to scan certain ports or targets.

