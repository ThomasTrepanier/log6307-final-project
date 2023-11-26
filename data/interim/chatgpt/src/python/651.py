import threading

# Parameters
NUM_THREADS = 10  # Adjust according to your hardware
UPPER_LIMIT_PER_THREAD = 10000000

# Pre-calculate FizzBuzz for the range 1-15
FIZZBUZZ_LOOKUP = [
    "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
]

def thread_fizz_buzz(thread_id):
    start = thread_id * UPPER_LIMIT_PER_THREAD
    end = start + UPPER_LIMIT_PER_THREAD
    
    result = []
    
    for i in range(start, end):
        # Use modulo 15 to get the repeating pattern
        result.append(FIZZBUZZ_LOOKUP[i % 15])
    
    # In a real-world scenario, you'd either append this to a shared data structure
    # or write this to a shared memory segment. This example simply returns it.
    return result

if __name__ == "__main__":
    threads = []
    results = [None] * NUM_THREADS

    for i in range(NUM_THREADS):
        thread = threading.Thread(target=thread_fizz_buzz, args=(i,))
        threads.append(thread)
        thread.start()

    for i, thread in enumerate(threads):
        thread.join()
        results[i] = thread_fizz_buzz(i)
