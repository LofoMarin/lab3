import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.15', 5050))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection established from address {address}")
    clientSocket.send(bytes("Welcome", "utf-8"))
    clientSocket.close()