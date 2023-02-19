import socket
import sys

s = socket.socket()

s.connect(('127.0.0.1', 8080))
s.send(b'GET / HTTP/1.0\r\n\r\n')
received_object = s.recv(200)
print(received_object)
s.close()
sys.exit()


