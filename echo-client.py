import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Enter Message: ")
        fmsg = bytes(msg, 'UTF-8')
        s.sendall(fmsg)
        data = s.recv(1024)
        print('[CLIENT] Received back from server: ', data.decode('UTF-8'))
