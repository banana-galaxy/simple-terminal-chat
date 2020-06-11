import socket, random

running = True

print("launching server")
IP = "127.0.0.1"
PORT = random.randint(8000, 9000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))
print(f"server connected\nPort: {PORT}")

windows = []
try:
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode().split("|")
        if data[0] == "window":
            windows.append(addr)
            #sock.sendto(str.encode("1"), addr)  # enable if data loss present
        elif data[0] == "client":
            for window in windows:
                sock.sendto(str.encode(data[1]), window)
except KeyboardInterrupt:
    sock.shutdown()
    sock.close()