from threading import Timer


def hello():
    print("hello, world")


t = Timer(5, hello)
t.start()
