import threading
import time

n = 100


class Producer(threading.Thread):
    def __init__(self, condition):
        super().__init__()
        self.condition = condition
        self.condition.current_number = 0

    def run(self):
        # print("producer started")
        for i in range(n+2):
            # +2 is needed to execute exit condition in Consumers.
            self.condition.current_number += 1
            with self.condition:
                # print("producer make resource available")
                # print("notifying one thread")

                self.condition.notify(1)
            time.sleep(0.1)


class Consumer(threading.Thread):
    def __init__(self, name, condition):
        threading.Thread.__init__(self)
        self.name = name
        self.condition = condition

    def run(self):
        # print("consumer started")
        consumed = 0
        while consumed <= n:
            with self.condition:
                # print("consumer waiting")
                self.condition.wait()
            consumed = self.condition.current_number
            print(f"consumer {self.name} consumed {consumed}")


cond = threading.Condition()
cs1 = Consumer("consumer-1", cond)
cs2 = Consumer("consumer-2", cond)
pd = Producer(cond)

cs1.start()
time.sleep(0.1)
cs2.start()
time.sleep(0.1)
pd.start()

cs1.join()
cs2.join()
pd.join()
