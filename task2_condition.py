import threading
import time
import logging


n=10

def consumer(cv):
    print("consumer started")
    with cv:
        print("consumer waiting")
        cv.wait()
        print("consumer consumed")

def producer(cv):
    print("producer started")
    with cv:
        print("producer make resource available")
        print("notifying all customers")
        cv.notifyAll()


class Producer(threading.Thread):
    def __init__(self, condition):
        super().__init__()
        self.condition = condition
        self.current_number = None

    def run(self):
        print('Producer thread started ...')
        # for i in range(n + 1):
        #     self.current_number = i
        print("Producer", self.condition._lock)
        self.condition.notifyAll()


class Consumer(threading.Thread):
    def __init__(self, name, starting, condition):
        threading.Thread.__init__(self)
        self.name = name
        self.current = starting
        self.condition = condition

    def run(self):
        print("consumer started")
        with self.condition:
            print("consumer waiting")
            self.condition.wait()
            print("consumer consumed")


cond = threading.Condition()
cs1 = Consumer("consumer-1", 0, cond)
cs2 = Consumer("consumer-2", 1, cond)
# pd = Producer(cond) #threading.Thread(name='producer', target=producer, args=(condition,))
#cs1 = threading.Thread(name='consumer1', target=consumer, args=(cond,))
#cs2 = threading.Thread(name='consumer2', target=consumer, args=(cond,))
pd = threading.Thread(name='producer', target=producer, args=(cond,))

cs1.start()
time.sleep(2)
cs2.start()
time.sleep(2)
pd.start()

#cs1.join()
#cs2.join()
#pd.join()