import socket

host = socket.gethostname()
port = 8000

sock = socket.socket()
sock.connect((host, port))

num_ques = 10

for _ in range(num_ques):
    recv_ques = sock.recv(1024).decode()
    print(recv_ques)
    my_ans = input('> ')
    sock.send(my_ans.encode())

score = sock.recv(1024).decode()
print('score is', score)