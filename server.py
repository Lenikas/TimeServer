import socket
from datetime import datetime
import base64
import time


def get_config():
    with open('configuration.txt', 'r') as f:
        try:
            fake_seconds = int(f.read().replace("\n", ""))
        except ValueError:
            print('Data in configuration file must be a number')
            exit(1)
    return fake_seconds


def start_server():
    fake_seconds = get_config()
    while True:
        current_time = datetime.now()
        current_time_seconds = time.mktime(current_time.timetuple())
        fake_time_seconds = current_time_seconds + fake_seconds
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(base64.b64encode(repr(fake_time_seconds)), (UDP_IP, UDP_PORT))


if __name__ == '__main__':
    UDP_IP = "localhost"
    UDP_PORT = 123
    print("UDP target host:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    start_server()
