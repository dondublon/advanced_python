import threading
import time


def foo(ev):
    print('Foo', end='')
    ev.set()


def bar(ev):
    while not ev.is_set():
        print('Waiting ...')
        ev.wait(1)
    print('Bar')


print_event = threading.Event()
ft = threading.Thread(name='foo', target=foo, args=(print_event,))
bt = threading.Thread(name='bar', target=bar, args=(print_event,))
bt.start()
time.sleep(3)
ft.start()