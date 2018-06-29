from queue import Queue
import time
import threading


in_queue = Queue(1)

def consumer():
    in_queue.get()
    print("Consumer got 1")
    in_queue.get()
    print("Consumer got 2")
    in_queue.task_done()


thread = threading.Thread(target=consumer)
thread.start()

in_queue.put(object())
print("Producer put 1")
in_queue.put(object())
print("Producer put 2")
thread.join()

print("Done")

