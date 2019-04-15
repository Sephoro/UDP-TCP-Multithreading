from socket import *

serverName =  'localhost' # '10.30.47.130'    # "10.196.6.147" #My IP adress #10.30.44.57 i
serverPort = 12550

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))



while True:


    message = input('Input message: ')
    
    if message == 'close': break

    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    print('From Server: ', modifiedMessage.decode())

clientSocket.close()
