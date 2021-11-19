import socket

s = socket.socket()
host = input("Please enter the host address : ")
port = 8080
s.connect((host, port))
print("Connected")

filename = input("Please enter the filename for the incomming file : ")
file = open(filename, 'wb')
file_data = s.recv(1024*3000)
file.write(file_data)
file.close()
print("File received successfully")
