import socket

HOST = 'localhost'
PORT = 2500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    number = int(input("Enter a number that you want to find factorial"))