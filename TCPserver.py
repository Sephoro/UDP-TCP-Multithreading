from socket import *
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        print(self)
        TCPServer(self.name)
        print("Exiting " + self.name)


serverPort = 12550
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

threads = []

def TCPServer(threadName):
    while True:
            
        message = connectionSocket.recv(1024).decode()
    
        if message == 'close' or '': break
        
        if message != '':
            print('\nMessage-->' + threadName + ':\n\"' + message + '\"\nSender: \n' + str(addr))

        modMessage = message.upper()
        connectionSocket.send(modMessage.encode())
        #connectionSocket.close()

count = 0


while True:
    
    count = count + 1

    serverSocket.listen(5)
    print('The server is ready to recieve on multiple thread: ')
    connectionSocket, addr = serverSocket.accept()
    thread_ = myThread(count, "Thread-" + str(count))
    thread_.start()    
    threads.append(thread_)

    connectionSocket.close()
    

#Create Threads

for thread_ in threads:
    thread_.join()