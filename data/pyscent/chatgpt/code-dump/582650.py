import threading

# Parameters
NUM_THREADS = 10  # Adjust according to your hardware
UPPER_LIMIT_PER_THREAD = 10000000

def fizz_buzz(start, end):
    result = []
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def thread_fizz_buzz(thread_id):
    start = thread_id * UPPER_LIMIT_PER_THREAD
    end = start + UPPER_LIMIT_PER_THREAD
    return fizz_buzz(start, end)

if __name__ == "__main__":
    threads = []
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=thread_fizz_buzz, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
