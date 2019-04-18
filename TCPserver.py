from socket import *
import threading

exitFlag = 0

class serverThreads  (threading.Thread):
    def __init__(self, threadID, name, connectionSocket, senderAddress):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.connectionSocket = connectionSocket
        self.senderAddress = senderAddress

    def run(self):
        print("Starting " + self.name)
        self.TCPpipeline()
        print("Exiting " + self.name)
        
    def TCPpipeline(self):
        while True:
            message = self.connectionSocket.recv(1024).decode()
            if message == 'close' or '': break
            if message != '':
                print('\nMessage-->' + self.name + ':\n\"' + message + '\"\nSender: \n' + str(self.senderAddress))
                
            modMessage = message.upper()
            connectionSocket.send(modMessage.encode())
	

#Setup 
serverPort = 20040
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
   
threads = []
count = 0 #House keeping

#Wait for contact

while True:
    
    count = count + 1

    serverSocket.listen(5)
    print('The server is ready to recieve on multiple threads: ')
    connectionSocket, addr = serverSocket.accept()
    thread_ = serverThreads(count, "Thread-" + str(count),connectionSocket, addr)
    thread_.start()    
    threads.append(thread_)

    #connectionSocket.close()
    
#Join threads in conclusion
for thread_ in threads:
    thread_.join()

connectionSocket.close()
