import threading
import time


n=10

# def consumer(cv):
#     print("consumer started")
#     with cv:
#         print("consumer waiting")
#         cv.wait()
#         print("consumer consumed")
#
# def producer(cv):
#     print("producer started")
#     with cv:
#         print("producer make resource available")
#         print("notifying all customers")
#         cv.notifyAll()


class Producer(threading.Thread):
    def __init__(self, condition):
        super().__init__()
        self.condition = condition
        self.condition.current_number = 0

    def run(self):
        print("producer started")
        for i in range(n):
            self.condition.current_number += 1
            with self.condition:
                print("producer make resource available")
                print("notifying one thread")

                self.condition.notify(1)
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, name, starting, condition):
        threading.Thread.__init__(self)
        self.name = name
        self.current = starting
        self.condition = condition

    def run(self):
        print("consumer started")
        while True:
            with self.condition:
                print("consumer waiting")
                self.condition.wait()
            print(f"consumer {self.name} consumed {self.condition.current_number}")


cond = threading.Condition()
cs1 = Consumer("consumer-1", 0, cond)
cs2 = Consumer("consumer-2", 1, cond)
pd = Producer(cond) #threading.Thread(name='producer', target=producer, args=(condition,))
#cs1 = threading.Thread(name='consumer1', target=consumer, args=(cond,))
#cs2 = threading.Thread(name='consumer2', target=consumer, args=(cond,))
# pd = threading.Thread(name='producer', target=producer, args=(cond,))

cs1.start()
time.sleep(1)
cs2.start()
time.sleep(1)
pd.start()

#cs1.join()
#cs2.join()
#pd.join()