import socket
s=socket.socket()

print('socket created')
s.bind(('localhost',5000))
s.listen(1)
print('waiting for connection',s)

while True:
    a,address=s.accept()
    print('connected with address',address)
    print('connected with',a)
    b=a.recv(1024).decode()
    print('.....',b)