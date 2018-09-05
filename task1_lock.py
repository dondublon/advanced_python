import threading
import time


n = 100


class MyThread (threading.Thread):
    thread_lock = threading.Lock()

    def __init__(self, name, starting):
        threading.Thread.__init__(self)
        self.name = name
        self.current = starting

    def run(self):
        while self.current <= n:
            MyThread.thread_lock.acquire()
            print(self.name, self.current)
            self.current += 2
            # Free lock to allow another thread work
            time.sleep(0.1)  # take a time to output our number.
            MyThread.thread_lock.release()
            time.sleep(0.1)  # allow another thread to output his number.


threads = [MyThread("Thread-1", 0), MyThread("Thread-2", 1)]
# Start all threads
for x in threads:
    time.sleep(0.05)  # to be sure that threads are starting in correct order.
    x.start()
# Start and wait for all threads to complete
for x in threads:
    x.join()
print("Exiting Main Thread")
