import socket


def func(data):
    try:
        op1, op, op2 = data.split()
        op1, op2, op = int(op1), int(op2), op.decode("utf-8")
        print(op1, op2, op)
    except:
        return b"Invalid operation"
    res = 0

    if(op == '+'):
        res = op1 + op2
    if(op == '-'):
        res = op1 - op2
    if(op == '*'):
        res = op1 * op2
    if(op == '/'):
        if(op2 != 0):
            res = op1 / op2
        else:
            res = "Invalid operation. Div by 0"

    return bytes(str(res), 'utf-8')


HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server Listening...")
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            msg = b"send input like 'operand' 'op' 'operand'"
            conn.sendall(msg)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                res = func(data)
                conn.sendall(res)
