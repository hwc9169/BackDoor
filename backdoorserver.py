import socket
import sys

BUF_SIZE = 1024
port = 10000
host = '127.0.0.1'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(10)
conn , addr = s.accept()
print("connected by " + addr[0])
pwd = conn.recv(BUF_SIZE).decode('utf-8')
print (pwd)

while (1) :
     cmd = input("Input command [exit] : ")
     if cmd == 'exit' :
          break;
     conn.send(cmd.encode('utf-8'))
     data = conn.recv(BUF_SIZE).decode('cp949')
     print(data)

s.close()


