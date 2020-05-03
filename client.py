import socket
import base64
from datetime import datetime

UDP_IP = "localhost"
UDP_PORT = 123


def start_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        received_time = datetime.fromtimestamp(float(base64.b64decode(data))).strftime("%A, %B %d, %Y %I:%M:%S")
        print("time from server:", received_time)


if __name__ == '__main__':
    start_client()