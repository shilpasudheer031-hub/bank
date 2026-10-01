import socket
c=socket.socket()
c.connect(('localhost',5000))

name=input("enter your name:")
c.send(bytes(name,'utf-8'))