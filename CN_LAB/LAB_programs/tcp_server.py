import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('120.0.0.1', 6265)

server_socket.bind(server_address)

server_socket.listen(5)

print("1. Listening...")

conn, addr = server_socket.accept()

print("Connection established with {0}".format(addr))

data = conn.recv(1024)

print("2. Data received: {0}".format(data.decode()))

message = "Hi This is server\n"

print("3. Sending data to client...")

conn.send(message.encode())

conn.close()

server_socket.close()