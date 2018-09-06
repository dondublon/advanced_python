import threading
import time

n = 100


def foo(ev):
    print('Foo', end='')
    ev.set()


class MyThread(threading.Thread):
    def __init__(self, name, ev, starting):
        super().__init__()
        self.name = name
        self.current = starting
        self.ev = ev

    def run(self):
        while self.current <= n:
            if not self.ev.is_set():
                # print('Waiting ...')
                self.ev.wait(1)
            self.ev.clear()
            print(self.name, self.current)
            self.current += 2
            time.sleep(0.1)
            self.ev.set()
            time.sleep(0.1)  # give another thread time to check the event.


my_event = threading.Event()
t1 = MyThread("thread-1", my_event, 0)
t2 = MyThread("thread-2", my_event, 1)
t1.start()
time.sleep(0.1)
t2.start()

t1.join()
t2.join()
