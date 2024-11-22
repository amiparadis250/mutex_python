import threading
import time

# Create a mutex
mutex = threading.Lock()

# Function to access shared resource
def get_data(cnt):
    # Acquire the mutex to ensure mutual exclusion
    mutex.acquire()
    try:
        thread_id = threading.get_ident()  # Get current thread ID
        time.sleep(0.5)  # Simulate processing
        print(f"Count: {cnt} (thread {thread_id})")
    finally:
        mutex.release()  # Release the mutex

# Main execution
count = 1
max_count = 10
while True:
    # Create and start a thread
    thread = threading.Thread(target=get_data, args=(count,))
    thread.start()
    count += 1
    if count > max_count:
        break
