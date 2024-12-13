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

## Code Explanation

### Modules Imported
- **`socket`**: Provides access to low-level networking interfaces. Used to create and manage network connections for both TCP and UDP scans.
- **`time`**: Used for setting timeouts and managing delays during network operations.
- **`argparse`**: Facilitates the creation of command-line interfaces for parsing and validating user-provided arguments.

### Function: `parse_args()`
- **Purpose**: Parses and validates the command-line arguments provided by the user.
- **Details**:
  - Uses `argparse.ArgumentParser` to define the CLI structure.
  - Accepts `target` (positional argument) for specifying the hostname or IP.
  - Requires `-p/--ports` to define ports to scan.
  - Includes optional flags `-sT` for TCP scans and `-sU` for UDP scans.

### Function: `parse_port_range(port_range)`
- **Purpose**: Converts user-defined port inputs into a list of integers for easy iteration.
- **Details**:
  - Supports comma-separated ports (e.g., `80,443`), ranges (e.g., `20-25`), and single ports (e.g., `22`).
  - Returns a list of port numbers for scanning.

### Function: `tcp_scan(target, ports)`
- **Purpose**: Scans specified TCP ports on the target.
- **Details**:
  - Creates a socket for each port with `socket.socket()`.
  - Attempts to connect to the port using `connect_ex()`.
  - Uses `settimeout(1)` to limit each attempt to 1 second.
  - Prints whether the port is open or closed based on the connection result.

### Function: `udp_scan(target, ports)`
- **Purpose**: Scans specified UDP ports on the target.
- **Details**:
  - Sends an empty packet to each port using `sendto()`.
  - Waits for a response with `recvfrom()`, handling potential timeouts or errors.
  - Reports whether the port is open, filtered, or unresponsive.

### Function: `main()`
- **Purpose**: Orchestrates the program by processing arguments and invoking the appropriate scan functions.
- **Details**:
  - Parses command-line arguments using `parse_args()`.
  - Extracts the target and ports, then determines which scans to perform based on flags.
  - Calls `tcp_scan()` and/or `udp_scan()` accordingly.

### Script Execution
- The `if __name__ == "__main__":` block ensures the script runs only when executed directly.
- Invokes the `main()` function to begin the scanning process.

## How It Works
1. **Run the Script**:
   Example: `python3 mynmap.py example.com -p 20-25 -sT -sU`.
   - Target: `example.com`
   - Ports: `20-25`
   - Scans: Both TCP and UDP.
2. **Process Arguments**:
   - Extracts the target and ports, parsing ranges or lists.
3. **Perform Scans**:
   - **TCP Scan**: Connects to each port and checks if it is open.
   - **UDP Scan**: Sends test packets and observes responses.
4. **Output Results**:
   - Displays port statuses (open, closed, or filtered) in the console.
