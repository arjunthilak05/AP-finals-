import threading
import time

# Create a Lock object
lock = threading.Lock()

def first_person(l):
    l.acquire()  # Person one acquires the lock
    print("Person one occupies the room")
    time.sleep(1)  # Simulates time spent in the room
    print("Person one leaves the room")
    l.release()  # Person one releases the lock

def second_person(l):
    l.acquire()  # Person two waits until the lock is available
    print("Person two occupies the room")
    time.sleep(1)
    print("Person two leaves the room")
    l.release()  # Person two releases the lock

# Create threads with the same shared lock
t1 = threading.Thread(target=first_person, args=(lock,))
t2 = threading.Thread(target=second_person, args=(lock,))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both threads finished. Main program ends.")
