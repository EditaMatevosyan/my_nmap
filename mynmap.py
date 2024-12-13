import socket
import time

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Simple TCP/UDP Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g., 20-25)", required=True)
    parser.add_argument("-sT", help="Perform TCP scan", action="store_true")
    parser.add_argument("-sU", help="Perform UDP scan", action="store_true")
    return parser.parse_args()

def parse_port_range(port_range):
    ports = []
    if "," in port_range:
        ports = [int(port.strip()) for port in port_range.split(",")]
    elif "-" in port_range:
        start, end = map(int, port_range.split("-"))
        ports = list(range(start, end + 1))
    else:
        ports = [int(port_range)]
    return ports


def tcp_scan(target, ports):
    print(f"Starting TCP scan on {target}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"{port}/tcp open")
            else:
                print(f"{port}/tcp is closed")

def udp_scan(target, ports):
    print(f"Starting UDP scan on {target}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)
            try:
                s.sendto(b"", (target, port))
                s.recvfrom(1024)
                print(f"{port}/udp open or filtered")
            except socket.timeout:
                print(f"{port}/udp filtered (no response)")
            except Exception as e:
                print(f"Error on UDP Port {port}: {e}")

def main():
    args = parse_args()
    target = args.target
    ports = parse_port_range(args.ports)

    if args.sT:
        tcp_scan(target, ports)
    if args.sU:
        udp_scan(target, ports)

if __name__ == "__main__":
    main()
