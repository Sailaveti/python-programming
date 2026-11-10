import socket

HOST = "127.0.0.1"
PORT = 6265
BUF = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hi This is UDP client\n"

s.sendto(msg.encode(), (HOST, PORT))

print("1. Message sent to server.")

data, addr = s.recvfrom(BUF)

print("2. Data received:", data.decode())

s.close()