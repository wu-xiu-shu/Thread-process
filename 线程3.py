#!/usr/bin/python
#coding: utf-8

'''
队列的 task_done 方法
队列中的数据的使用者用来指示对于项目的处理已经结束。
如果使用此方法，那么从队列中删除的每一项都应该调用一次。

队列中的 join 方法
阻塞直到队列中的所有项目均被删除和处理为止。
一旦为队列中的每一项都调用了一次 task_done 方法，此方法将直接返回
'''

import Queue
import threading

class WorkerQueue(threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        # 创建队列
        self.input_queue = Queue.Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        # 阻塞知道队列中的所有项目均被删除和处理为止
        self.input_queue.join()

    def run(self):
        while True:
            item = self.input_queue.get()
            if item is None:
                break

            # 输出结果
            print item
            self.input_queue.task_done()

        # 完成，指示受到和返回了标志
        self.input_queue.task_done()
        return

w = WorkerQueue()
w.start()
w.send("Hello, ")
w.send("World")
w.close()