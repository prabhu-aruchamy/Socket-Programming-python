import socket

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket()
s.connect((HOST, PORT))
data = s.recv(1024)
print(data.decode('utf-8'))
user_in = str(input("Enter an operation\n"))
inp = bytes(user_in, 'utf-8')
s.sendall(inp)
res = s.recv(1024)
print(res.decode('utf-8'))
