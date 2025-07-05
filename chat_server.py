import socket
import threading

#public socket creation
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5000
s.bind(("0.0.0.0",port))
s.listen(10)
c , addr = s.accept()

#handling threat event to stop the thread 
sharedthreat = threading.Event()

#method to send msg to client
def sendMsg():
    while not sharedthreat.is_set():
        try:
            msg = input("send : ")
            if(msg=="end"):           
                c.sendall(b"end")
                s.close()
                sharedthreat.set()
                break
            c.sendall(msg.encode())
        except:
            break

#method to receive msg from client
def recvMsg():
    while not sharedthreat.is_set():
        try:           
            msg = c.recv(1024).decode()
            if(msg=="end"):
                c.close()
                s.close()
                sharedthreat.set()
                break
            print(f"\nrecv : {msg}\nsend : ", end="")
        except:
            break
    

#call and use threading to run both recvMsg and sendMsg at same time
sendThreat = threading.Thread(target=sendMsg)
recvThreat = threading.Thread(target=recvMsg)
sendThreat.start()
recvThreat.start()



