import socket

# set up the socket with valid port number
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set up the connection
my_socket.connect(('data.pr4e.org', 80))

# encode the command into utf-8 from unicode string
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# send the command via socket
my_socket.send(cmd)

while True:
    # limit buffersize to 512, i.e len of data received
    data = my_socket.recv(512)
    if len(data) < 1:
        break

    print(data.decode(), end='')

# close the connection
my_socket.close()
