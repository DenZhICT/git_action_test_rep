import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 6565))
server.listen(1)
while True:
    con, adr = server.accept()
    data = con.recv(1024)
    if not data:
        con.close()
        break
    con.send(data)
    con.close()

server.close()
