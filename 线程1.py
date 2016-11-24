#!/usr/bin/python
#coding: utf-8

import threading
import time

# 自定义的线程类要继承自threading.Thread，要重写__init__和run两个方法，
# run方法在线程类运行的时候会自动运行，不需要调用

class MyThread(threading.Thread):

    def __init__(self, threadName):
        # 继承
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print("Starting " + self.threadName)

        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        lock.acquire()
        func(self.threadName, 1, 5)
        # 释放锁
        lock.release()

        print("Exiting " + self.threadName)

def func(name, delay, count):
    while count:
        time.sleep(delay)
        count -= 1
        print(name + "is running")

# 创建线程锁
lock = threading.Lock()

thread1 = MyThread("thread - 1")
thread2 = MyThread("thread - 2")

# 启动线程
thread1.start()
thread2.start()

print("Exiting Main Thread")
