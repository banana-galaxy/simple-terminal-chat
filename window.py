import socket

IP = "127.0.0.1"
PORT = int(input("Port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(str.encode("window|"), (IP, PORT))
try:
    while True:
        data, addr = sock.recvfrom(1024)
        print(data.decode())
except KeyboardInterrupt:
    sock.shutdown()
    sock.close()