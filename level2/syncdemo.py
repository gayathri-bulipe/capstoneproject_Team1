from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good evening",end=" ")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=('Jose',))
t2=Thread(target=wish,args=('Mich',))
t3=Thread(target=wish,args=('Mart',))
t1.start()
t2.start()
t3.start()