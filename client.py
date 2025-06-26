import socket
lhost = 'localhost'
port=80
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((lhost,port))
    s.close()
except Exception as e:
    print("failed ",e)
