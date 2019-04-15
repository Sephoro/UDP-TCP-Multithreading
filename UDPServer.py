from socket import *
import threading
import time
import os

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        print(self)
        UDPServer(self.name)
        print("Exiting " + self.name)

""" def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        #os.system('clear')
        print("%s: %s %d" % (threadName, time.ctime(time.time()),counter))
        print(threading.active_count()) #,threading.current_thread())
        counter -= 1
 """

#The UDP server

def UDPServer(threadName):

    serverPort = 12050
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    serverSocket.bind(('',serverPort))


    print("The sever is ready to receive on thread : " + threadName + "\n\n\n")

    while True:

       message,clientAddress = serverSocket.recvfrom(2048)
       print(message.decode())
       modifiedMessage = message.decode().upper()
       serverSocket.sendto(modifiedMessage.encode(), clientAddress)

#Create Threads

threads = []

for i in range(1,3):
    
    thread = myThread(i,"Thread-" + str(i))
    threads.append(thread)

#Start the threads

for i in range(0,2):

    threads[i].start()
    #print( threads[i].getName(), "\n\n")


print("Exiting Main Thread")