import socket

s = socket.socket()
port = 5005
li = input().split(" ")
print(li)
s.connect(('127.0.0.1', port))
size = int(s.recv(1024).decode())
i = 0
while i < len(li):
    if i == len(li) - 1:
        print("closing connection")
        s.send(li[i].encode())

        s.close()
        break
    s.send(li[i].encode())
    size = int(s.recv(1024).decode())
    print(size)
    while size <= 0 and i < len(li):
        size = int(s.recv(1024).decode())
    i = i + 1


