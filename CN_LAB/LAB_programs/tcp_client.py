import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 6265)

client_socket.connect(server_address)

print("1. Sending data to server...")

message = "Hi This is client\n"

client_socket.send(message.encode())

data = client_socket.recv(1024)

print("4. Data received: {0}".format(data.decode()))

client_socket.close()
