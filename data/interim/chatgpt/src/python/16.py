import bonobo
from bonobo.config import use
import concurrent.futures
import time

def generate_numbers(count: int) -> int:
    for i in range(count):
        yield i

def delayed_output(x: int) -> str:
    time.sleep(1)
    return f"Number: {x}"

def with_max_workers(max_workers):
    def decorator(f):
        def wrapper(*args, **kwargs):
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                yield from executor.map(f, *args, **kwargs)
        return wrapper
    return decorator

@use('count')
def get_numbers(count: int) -> int:
    yield from generate_numbers(count)

@with_max_workers(3)
def process_numbers(numbers: int) -> str:
    return delayed_output(numbers)

def print_output(output: str):
    print(output)

def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(
        get_numbers,
        process_numbers,
        print_output,
        _input=bonobo.Limit(1),  # We only want to process 1 input for this example
    )
    return graph

def run(count: int):
    bonobo.run(get_graph(count=count))

run(3)
#=> "Number: 0"
#=> "Number: 1"
#=> "Number: 2"
