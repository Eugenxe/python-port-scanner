import socket
import threading

hostname = input("Enter host:")
try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    print(f"The {hostname} is invalid")
    exit()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip_address, port))
    
    if result == 0:
        print(f"{port} is open")
    else:
        print(f"{port} is unreachable")
    s.close()

threads = []

for port in range (1, 101):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("scan complete")