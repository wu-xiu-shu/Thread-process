#!/usr/bin/python
#coding: utf-8

import Queue
import threading
import time

flag = 0

class Mythread(threading.Thread):

    def __init__(self, thread, que):
        threading.Thread.__init__(self)
        self.thread = thread
        self.que = que

    def run(self):
        print "Starting " + self.thread
        func(self.thread, self.que)
        print "Exiting " + self.thread

def func(name, que):
    # 如果说flag不为0，则证明此时队列中还有数据
    while not flag:
        lock.acquire()
        if not que.empty():
            data = que.get()
            lock.release()
            print("%s processing %s" % (name, data))
        else:
            lock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
lock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []

for _thread in threadList:
    thread = Mythread(_thread, workQueue)
    thread.start()
    threads.append(thread)

# 填充队列
lock.acquire()
for name in nameList:
    workQueue.put(name)
lock.release()

# 如果队列不为空，则停留在此处，等待队列为空
while not workQueue.empty():
    pass

# 要退出了
flag = 1

# 等待所有的线程都运行完
for t in threads:
    t.join()

print("Exiting Main Thread")