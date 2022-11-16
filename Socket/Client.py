import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5050))

message = s.recv(2048)

print(f"Message recived: {message}")

