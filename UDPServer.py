from socket import *
import threading
import time
import os

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, message, Address):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.message = message
        self.serverAddress = Address
    def run(self):
        print("Starting " + self.name)
        print(self)
        messaging(self.name, self.message, self.serverAddress)
        print("Exiting " + self.name)


#Setup

serverPort = 12055
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))


#For threads

def messaging(threadName, message, clientAddress):
    print(threadName + " in Action: \n")
    print(message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)



threads = []
count = 0 #House keeping

#Wait for contact

print("The sever is ready to receive using threads \n\n")

while True:
    count = count + 1
    message,clientAddress = serverSocket.recvfrom(2048)
    thread_ = myThread(count, "Thread-"+str(count), message, clientAddress)
    thread_.start()
    threads.append(thread_)

#Join threads for conclusion
for t in threads:
    t.join()       
