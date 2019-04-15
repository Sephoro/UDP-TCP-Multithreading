
from socket import *
serverName ='localhost' # "10.196.51.24" #IP adress / server website adress Mine: 10.30.44.14 #10.196.6.16
serverPort = 12050
# using clientSocket as cs

clientSocket = socket(AF_INET,SOCK_DGRAM) #creates client socket


while True:
        
	message = input('input lowercase sentence: ')
         
	if message == 'close' : break
		
	clientSocket.sendto(message.encode(), (serverName, serverPort))

	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

	print(modifiedMessage.decode())

clientSocket.close()




