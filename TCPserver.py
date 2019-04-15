from socket import *

serverPort = 12550

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('The server is ready to recieve\n\n')


while True:
    
    connectionSocket, addr = serverSocket.accept()

    while True:
        message = connectionSocket.recv(1024).decode()
    
        if message == 'close' or '': break
        
        if message != '':
            print('\nMessage : \n\"' + message + '\"\nSender: \n' + str(addr))

        modMessage = message.upper()
        connectionSocket.send(modMessage.encode())
     
    connectionSocket.close()
    break

'''
while True:
    
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    
    print('\nMessage : \n\"' + message + '\"\n\t\tSender: \n' + str(addr))

    modMessage = message.upper()
    connectionSocket.send(modMessage.encode())
    
    connectionSocket.close()

'''
