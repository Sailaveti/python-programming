import socket

HOST = "127.0.0.1"
PORT = 6265
BUF = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print("1. UDP server listening on " + HOST + ":" + str(PORT))

data, addr = s.recvfrom(BUF)

print("2. Data received:", data)

reply = "Hi This is UDP server\n"

s.sendto(reply.encode(), addr)

print("3. Reply sent to", addr)

s.close()