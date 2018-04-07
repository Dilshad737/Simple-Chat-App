from socket import *


s = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12221
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Waiting
       print ("[Waiting for connection...]")
       c, addr = s.accept()
       #print(c)
       print ('Got connection from', addr)
   else:
       # Waiting
       print ('[Waiting for response...]')
       print (c.recv(1024).decode())
       q = input("Enter something to this client: ")
       c.send(q.encode())
