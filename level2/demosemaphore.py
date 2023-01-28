from threading import *
import time
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("good evening",end=" ")
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Jose',))
t2=Thread(target=wish,args=('Mich',))
t3=Thread(target=wish,args=('Mart',))
t4=Thread(target=wish,args=('solomon',))
t5=Thread(target=wish,args=('Janu',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
