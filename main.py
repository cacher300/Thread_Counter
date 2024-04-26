import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(10)
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    threads = []
    try:
        while True:
            thread = threading.Thread(target=thread_function, args=(len(threads)+1,))
            thread.start()
            threads.append(thread)
            print(f"Started thread {len(threads)}")
    except Exception as e:
        print(f"Failed after starting {len(threads)} threads: {e}")

    for thread in threads:
        thread.join()
