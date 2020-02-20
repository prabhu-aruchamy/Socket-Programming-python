import socket
from _thread import start_new_thread


def client_handler(conn, addr):
    score = 0
    for ques, ans in ques_ans_dict.items():
        conn.send(ques.encode())
        recv_ans = conn.recv(1024).decode()

        if recv_ans == ans:
            score += 1
    conn.send(str(score).encode())
    conn.close()


# main
port = 8000
host = socket.gethostname()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(10)
print('Server has started succesfully. Running on port {}'.format(port))
connections = list()
ques_ans_dict = {}
for i in range(3):
    print("Enter the question:")
    ques = input()
    print("Enter the answer:")
    ans = input()
    ques_ans_dict[ques] = ans
while True:
    conn, addr = s.accept()
    connections.append(conn)
    print('Connected from address: {}'.format(str(addr)))
    start_new_thread(client_handler, (conn, addr))
s.close()
