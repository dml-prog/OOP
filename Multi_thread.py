from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)


s1 = hello()
s2 = hi()
s1.start()
sleep(.2)
s2.start()
s1.join()
s2.join()
print("byee")