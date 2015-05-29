import socket

__author__ = 'amatveev'


s = socket.socket()
s.bind(("localhost", 1111))
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Connection from ', addr
    c.close()