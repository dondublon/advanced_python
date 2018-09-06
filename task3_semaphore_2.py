import threading
import time

n = 100


class MyThread(threading.Thread):
    def __init__(self, name, semaphore, starting):
        threading.Thread.__init__(self)
        self.name = name
        self.sem = semaphore
        self.current = starting

    def run(self):
        # print("consumer started")
        while self.current <= n:
            self.sem.acquire()
            print(self.name, self.current)
            self.current += 2
            time.sleep(0.1)
            self.sem.release()
            time.sleep(0.1)


sem = threading.Semaphore(2)
cs1 = MyThread("thread-1", sem, 0)
cs2 = MyThread("thread-2", sem, 1)

cs1.start()
time.sleep(0.1)
cs2.start()
time.sleep(0.1)

cs1.join()
cs2.join()
