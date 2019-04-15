
#!/usr/bin/python


import threading
import time
import os

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        print("Starting " + self.name)
        print(self)
        print_time(self.name, self.counter, self.delay)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        #os.system('clear')
        print("%s: %s %d" % (threadName, time.ctime(time.time()),counter))
        print(threading.active_count()) #,threading.current_thread())
        counter -= 1


threads = []

#Create Threads


'''
for i in range(1,6):
    print(i)
'''
for i in range(1,6):
    
    thread = myThread(i,"Thread-" + str(i),5,i)
    threads.append(thread)

#Start the threads

for i in range(0,5):

    threads[i].start()
    print( threads[i].getName(), "\n\n")


print("Exiting Main Thread")


