import multiprocessing
from multiprocessing import Pool
import time
import typing

def work(doc: str) -> str:
    # do some processing here....
    return doc + " processed"

def download(url: str) -> str:
    return url  # a hack for demo, use e.g. `requests.get()`

def run_pipeline(
    urls: typing.List[str],
    session_request_limit: int = 10,
    session_length: int = 60,
) -> None:
    """
    Download and process each url in `urls` at a max. rate limit
    given by `session_request_limit / session_length`
    """
    workers = Pool(multiprocessing.cpu_count())
    results = []

    n_requests = 0
    session_start = time.time()

    for url in urls:
        doc = download(url)
        results.append(
            workers.apply_async(work, (doc,))
        )
        n_requests += 1

        if n_requests >= session_request_limit:
            time_to_next_session = session_length - time.time() - session_start
            time.sleep(time_to_next_session)

        if time.time() - session_start >= session_length:
            session_start = time.time()
            n_requests = 0

    # Collect results
    for result in results:
        print(result.get())

if __name__ == "__main__":
    urls = ["www.google.com", "www.stackoverflow.com"]
    run_pipeline(urls)
