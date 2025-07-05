import socket
import threading

#public socket creation
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5000
ip_addr = input("Enter server ip : ").strip()
s.connect((ip_addr,port))

#handling threat event to stop the thread 
sharedthreat = threading.Event()

#method to recv msg from server
def recvMsg():
    while not sharedthreat.is_set():
        try:      
            msg = s.recv(1024).decode()
            if(msg=="end"):
                s.close()
                sharedthreat.set()
                break
            print(f"\nrecv : {msg}\nsend : ", end="")
        except:
            break

#method to send msg to server
def sendMsg():
    while not sharedthreat.is_set():
        try:     
            msg = input("send : ")
            if(msg=="end"):
                s.sendall(b"end")
                s.close()
                sharedthreat.set()
                break
            s.sendall(msg.encode())
        except:
            break

#use threading to run both the methods to send and recv messages
recvThreat = threading.Thread(target=recvMsg)
sendThreat = threading.Thread(target=sendMsg)
recvThreat.start()
sendThreat.start()      



        


        