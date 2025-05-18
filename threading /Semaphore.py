import threading
import time

# Create a semaphore with 2 permits
sem = threading.Semaphore(2)

def worker(name):
    print(f"{name} is waiting to acquire the semaphore")
    with sem:  # Acquire the semaphore (decreases count)
        print(f"{name} has acquired the semaphore")
        time.sleep(2)  # Simulate work (resource usage) for 2 seconds
        print(f"{name} is releasing the semaphore")  # Semaphore will be released automatically here

# Create 5 threads trying to access the resource
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    t.start()
