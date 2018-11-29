import socket
import time
import random


def Main():


    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 5001))

    print('Server started')
    while True:
        time.sleep(3)
        print('...')
        data, addr = s.recvfrom(1024)
        print("message from: " + str(addr))
        print("from connected user: " + str(data))
        data = str(random.randrange(0, 1000000))
        print("sending: " + str(data))
        s.sendto(data.encode(), addr)
    s.close()

if __name__ == '__main__':
    Main()


