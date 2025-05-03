import socket

def scan_ports(target):
    """
    Scans ports 1-1024 on the given target and prints open ones.
    """
    print(f"\n[+] Scanning target: {target}")
    for port in range(1, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"[OPEN] Port {port}")
        except socket.gaierror:
            print(f"[ERROR] Invalid target: {target}")
            break
        except Exception as e:
            pass  # You can log this if needed

if __name__ == "__main__":
    target = input("Enter IP or domain: ")
    scan_ports(target)
