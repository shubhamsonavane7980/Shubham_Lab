import threading
import os

def task():
    thread_name = threading.current_thread().name
    process_id = os.getpid()
    print(f"Task executed by thread '{thread_name}' in process {process_id}.")

# Create four threads
threads = []
for i in range(4):
    t = threading.Thread(target=task)
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()