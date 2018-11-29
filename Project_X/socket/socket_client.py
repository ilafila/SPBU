import socket


def Main():
    server = ('127.0.0.1', 5001)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # try:
    #    s.bind(('127.0.0.1', 5001))
    #except:
     #   pass

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("recieved from server:" + str(data))
        message = input("-> ")
    s.close()


if __name__ == '__main__':
    Main()
