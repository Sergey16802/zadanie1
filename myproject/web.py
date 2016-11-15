import socket

BUFFER_SIZE = 1024

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.bind(("localhost", 8000))
SOCKET.listen(1)
 
while True:
    conn, addr = SOCKET.accept()
    data = conn.recv(BUFFER_SIZE)
    splt_data = data.split(' ')
    FILE = open(splt_data[1], 'rb')
    answer = FILE.read()
    FILE.close()
    conn.send("HTTP/1.1 200 OK \n" + answer)
conn.close()
SOCKET.close()