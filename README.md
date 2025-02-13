# mutex_python


# What is a Mutex?

A **mutex** (short for *mutual exclusion*) is a synchronization mechanism used in concurrent programming to prevent multiple threads or processes from simultaneously accessing a shared resource or critical section.

---

## Key Features of a Mutex

1. **Exclusive Access**:
   - Only one thread or process can hold the mutex at any given time.
   - Ensures safe access to shared resources.

2. **Blocking**:
   - If a thread/process tries to acquire a mutex that is already held, it is forced to wait until the mutex is released.

3. **Atomic Operations**:
   - Operations like acquiring and releasing a mutex are atomic, ensuring no intermediate states.

---

## Why is a Mutex Needed?

In concurrent environments, multiple threads or processes may:
- **Read and write shared data simultaneously**.
- **Cause race conditions**, where the output depends on the unpredictable sequence of thread execution.
- **Corrupt shared data**, leading to inconsistent or invalid states.

A mutex ensures that:
1. Only one thread/process can modify the resource at a time.
2. Other threads/processes must wait until the mutex is released.

---

## How a Mutex Works

1. **Locking**:
   - A thread/process locks the mutex before accessing the critical section.
   - This prevents other threads/processes from entering the critical section until the lock is released.

2. **Critical Section**:
   - Code that accesses shared resources is called the *critical section*. This section is executed exclusively by the thread holding the mutex.

3. **Unlocking**:
   - Once the thread/process finishes its task, it releases the mutex so that others can acquire it.

---

## Example of a Mutex in Python

Here is an example showing how a mutex works in Python using the `threading` module:

### Without Mutex (Race Condition)
```python
import threading

# Shared resource
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # Race condition

threads = []
for _ in range(2):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final Counter:", counter)  # Output is unpredictable
