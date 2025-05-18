import threading
import time

count = 0
lock = threading.Lock()

def counter(name):
    global count

    print(name, "starting count")
    for i in range(1000000):
        lock.acquire()
        count += 1
        lock.release()

    print(name, "count STOPPED")

Dinesh = threading.Thread(target=counter, args=["Dinesh"])
Deepak = threading.Thread(target=counter, args=["Deepak"])

Dinesh.start()
Deepak.start()

Dinesh.join()
Deepak.join()

print("Final count is", count)
