import socket

IP = "127.0.0.1"
PORT = int(input("Port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nick = input("nickname: ")
sock.sendto(str.encode(f"client|{nick} joined the chat"), (IP, PORT))
try:
    while True:
        sock.sendto(str.encode(f"client|{nick}: {input()}"), (IP, PORT))
except KeyboardInterrupt:
    sock.sendto(str.encode(f"client|{nick} left the chat"), (IP, PORT))
    sock.shutdown()
    sock.close()