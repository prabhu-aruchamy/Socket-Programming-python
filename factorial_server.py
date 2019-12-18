import socket
import math

# def facto(number):
#     number = int(number.decode('UTF-8'))
#     factorial(number)
#     return number

#main


HOST = 'localhost'
PORT = 2500
s = socket.socket()

s.bind((HOST, PORT))
s.listen()
print("Server Listening at port", PORT)
while True:
    conn, addr = s.accept()
    with conn:
        print("Connected in", addr)
        while True:
            num = conn.recv(3000)
            if not num:
                break
            num = num.decode('UTF-8')
            res = math.factorial(int(num))
            print("res= ", res)
            res = bytes(str(res), 'UTF-8')
            conn.sendall(res)


