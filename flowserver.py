import socket

s=socket.socket()
print("socket created")
port=5005

s.bind(('',port))
print("socket binded to port %s"%(port))

s.listen(5)
print("socket is listening")
recv_window=[]
print("Enter recieve window size")
size=int(input())
lent =size
c,addr=s.accept()
print("got connection from ",addr)
c.send(str(size).encode())
a=""

while a!='end':
    a=str(c.recv(1024).decode())
    recv_window.append(a)
    if a!='end':
        print(a)
    size=size-1

    if size==0 and a!='end':
        c.send(str(size).encode())
        i=0
        while i<1:
            print("application running")
            size=size+1
            i=i+1
    if a!='end':
        c.send(str(size).encode())
    
print("closing connection")
s.close()


