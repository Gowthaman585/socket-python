import socket

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port = 80
    s.bind(("",port))
    s.listen(2)
    while True:
        c,address = s.accept()
        print(f'detected the ip and port : {address}')
        print(c)
except socket.error as err:
    print("Failed")
