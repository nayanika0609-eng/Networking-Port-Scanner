import socket
import threading

print("⚡ Advanced Multi-Threaded Port Scanner")

# User inputs only IP address
target_ip = input("Enter the IP address to scan: ")

# User enters port range
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

# Thread lock for clean output
print_lock = threading.Lock()

def scan_port(port):
    """Function to scan a single port."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))

        with print_lock:
            if result == 0:
                print(f"Port {port} ➜ OPEN")
            # If you want to show closed ports, uncomment:
            # else:
            #     print(f"Port {port} ➜ CLOSED")

        sock.close()

    except KeyboardInterrupt:
        print("Scan stopped.")
        exit()
    except socket.gaierror:
        print("Invalid IP address.")
        exit()
    except socket.error:
        print("Connection error.")
        exit()

# Create threads for each port
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("\nScan complete ✔")
