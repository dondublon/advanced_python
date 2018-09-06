from threading import Timer
import time

n = 100
tick = 0.1

# I use "pseudo-threads" -
# Timer that invokes another timer in his working function.


def print_num(name, number):
    print("pseudo-thread name:", name, number)
    if number + 1 < n:
        t = Timer(tick * 2, function=print_num, args=(name, number + 2))
        t.start()


t1 = Timer(0, print_num, args=("1", 0))
t2 = Timer(0, print_num, args=("1", 1))
t1.start()
time.sleep(tick)
t2.start()
