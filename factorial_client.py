import socket

HOST = 'localhost'
PORT = 2500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    number = input("Enter a number that you want to find factorial: ")
    number = bytes(number, 'UTF-8')
    s.sendall(number)
    res = s.recv(3000)
    print("The Factorial of the number", number.decode('UTF-8'), "is", res.decode('UTF-8'))
