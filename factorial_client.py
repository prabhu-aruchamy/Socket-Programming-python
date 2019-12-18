import socket

HOST = 'localhost'
PORT = 2500

s = socket.socket()
s.connect((HOST, PORT))
while True:
    number = input("Enter a number that you want to find factorial: ")
    number = bytes(number, 'UTF-8')
    s.sendall(number)
    res = s.recv(3000)
    print("The Factorial of the number", number.decode('UTF-8'), "is", res.decode('UTF-8'))
