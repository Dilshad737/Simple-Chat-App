from socket import *

s = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 12221
print("Developed By Dilshad Ali Chattha")
s.connect((host, port))
print ("Now you are connected to: ", host)

while True:
    z = input("Send your message to the server: ")
    s.send(z.encode())
    # Waiting
    print ('[Waiting for response...]')
    print (s.recv(1024).decode())
